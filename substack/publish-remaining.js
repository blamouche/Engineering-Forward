const fs = require('fs');
const path = require('path');

const substackDir = __dirname;
const cookies = JSON.parse(fs.readFileSync(path.join(substackDir, 'substack_cookies.json'), 'utf-8'));
const cookieStr = Object.entries(cookies).map(([k,v]) => `${k}=${v}`).join('; ');
const BASE = 'https://engineeringforward.substack.com';

async function apiCall(method, url, body) {
  const opts = { method, headers: { 'Cookie': cookieStr, 'Content-Type': 'application/json' } };
  if (body) opts.body = JSON.stringify(body);
  const resp = await fetch(BASE + url, opts);
  return resp;
}

function buildJSON(md) {
  const mdLines = md.split('\n');
  const content = [];
  for (let i = 0; i < mdLines.length; i++) {
    const t = mdLines[i].trim();
    if (!t) continue;
    if (t.startsWith('## ')) {
      content.push({ type: 'heading', attrs: { level: 2 }, content: [{ type: 'text', text: t.slice(3).trim() }] });
    } else if (t === '---') {
      content.push({ type: 'horizontalRule' });
    } else if (t.match(/^\d+\.\s+\[.*\]\(.*\)$/)) {
      const match = t.match(/^(\d+)\.\s+\[(.*?)\]\((.*?)\)$/);
      content.push({ type: 'paragraph', attrs: { textAlign: null }, content: [
        { type: 'text', text: match[1] + '. ' },
        { type: 'text', text: match[2], marks: [{ type: 'link', attrs: { href: match[3] } }] }
      ]});
    } else {
      const parts = [];
      let remaining = t;
      const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
      let lastIndex = 0;
      let match;
      while ((match = linkRegex.exec(remaining)) !== null) {
        if (match.index > lastIndex) parts.push({ type: 'text', text: remaining.slice(lastIndex, match.index) });
        parts.push({ type: 'text', text: match[1], marks: [{ type: 'link', attrs: { href: match[2] } }] });
        lastIndex = match.index + match[0].length;
      }
      if (lastIndex < remaining.length) parts.push({ type: 'text', text: remaining.slice(lastIndex) });
      if (parts.length === 0) parts.push({ type: 'text', text: t });
      content.push({ type: 'paragraph', attrs: { textAlign: null }, content: parts });
    }
  }
  return { type: 'doc', content };
}

function extractBody(markdown) {
  const lines = markdown.split('\n');
  let bodyStart = 0, bodyEnd = lines.length;
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].match(/^\*(.+)\*$/)) { bodyStart = i + 1; break; }
  }
  for (let i = bodyStart; i < lines.length; i++) {
    if (lines[i].trim() === '---') { bodyEnd = i; break; }
  }
  return lines.slice(bodyStart, bodyEnd).join('\n').trim();
}

async function publishPost(filepath) {
  const markdown = fs.readFileSync(filepath, 'utf-8');
  const title = markdown.match(/^# (.+)$/m)[1].trim();
  const subtitleMatch = markdown.match(/^\*(.+)\*$/m);
  const subtitle = subtitleMatch ? subtitleMatch[1].trim() : '';
  const bodyJSON = buildJSON(extractBody(markdown));
  
  const slug = title.toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');

  // 1. Create draft
  const createResp = await apiCall('POST', '/api/v1/drafts', {
    draft_title: title,
    draft_subtitle: subtitle,
    draft_body: JSON.stringify(bodyJSON),
    type: 'newsletter',
    audience: 'everyone',
    draft_bylines: [{ id: 26001927, is_guest: false }],
    should_send_email: false,
    should_send_free_preview: false,
  });

  if (createResp.status === 429) return { success: false, rate_limited: true };
  const createData = await createResp.json();
  if (createResp.status !== 200) {
    return { success: false, title, error: `Create: ${JSON.stringify(createData).slice(0, 200)}` };
  }

  let draftId = createData.id;

  // 2. Set slug
  await apiCall('PUT', `/api/v1/drafts/${draftId}`, { slug });

  // 3. Publish
  const publishResp = await apiCall('POST', `/api/v1/drafts/${draftId}/publish`);
  
  if (publishResp.status === 200) {
    return { success: true, title, url: `https://engineeringforward.substack.com/p/${slug}` };
  } else {
    return { success: false, title, error: `Publish: ${publishResp.status}` };
  }
}

(async () => {
  // Only the 16 that failed due to rate limiting
  const toPublish = [
    '20260521-post-ais-third-act-is-about-who-owns-the-plumbing.md',
    '20260526-post-ais-implementation-gap.md',
    '20260824-post-the-true-price-of-intelligence-is-showing.md',
    '20260825-post-the-companies-that-know-what-not-to-do.md',
    '20260826-post-the-model-is-not-the-product.md',
    '20260827-post-the-calculator-defense.md',
    '20260828-post-the-two-week-migration.md',
    '20260829-post-the-thirty-trillion-dollar-cron-job.md',
    '20260830-post-the-parts-that-dont-write-themselves.md',
    '20260831-post-own-the-judgment-rent-the-rest.md',
    '20260901-post-the-companies-building-what-they-cant-buy.md',
    '20260902-post-the-flood-and-the-filter.md',
    '20260903-post-the-method-walks-out-the-door.md',
    '20260904-post-the-loop-eats-its-own.md',
    '20260906-post-the-stack-settles.md',
    '20260907-post-the-output-you-cant-trust.md',
  ];

  let published_count = 0;
  let failed_count = 0;

  for (const f of toPublish) {
    const filepath = path.join(substackDir, f);
    if (!fs.existsSync(filepath)) {
      console.log(`SKIP (not found): ${f}`);
      continue;
    }

    const markdown = fs.readFileSync(filepath, 'utf-8');
    const title = markdown.match(/^# (.+)$/m)[1].trim();
    console.log(`\n[${published_count + failed_count + 1}] Publishing: ${title}`);
    
    try {
      const result = await publishPost(filepath);
      if (result.success) {
        console.log(`  ✅ ${result.url}`);
        published_count++;
      } else if (result.rate_limited) {
        console.log(`  ⏳ Rate limited. Waiting 60s...`);
        await new Promise(r => setTimeout(r, 60000));
        // Retry once
        const result2 = await publishPost(filepath);
        if (result2.success) {
          console.log(`  ✅ ${result2.url}`);
          published_count++;
        } else {
          console.log(`  ❌ ${result2.error || 'Still rate limited'}`);
          failed_count++;
          // Wait longer before next
          await new Promise(r => setTimeout(r, 60000));
        }
      } else {
        console.log(`  ❌ ${result.error}`);
        failed_count++;
      }
    } catch (e) {
      console.log(`  ❌ ${e.message}`);
      failed_count++;
    }

    // 3s delay between posts
    await new Promise(r => setTimeout(r, 3000));
  }

  console.log(`\n=== Published: ${published_count} | Failed: ${failed_count} ===`);
})();