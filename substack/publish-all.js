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
  const draftBody = {
    draft_title: title,
    draft_subtitle: subtitle,
    draft_body: JSON.stringify(bodyJSON),
    type: 'newsletter',
    audience: 'everyone',
    draft_bylines: [{ id: 26001927, is_guest: false }],
    should_send_email: false,
    should_send_free_preview: false,
  };

  const createResp = await apiCall('POST', '/api/v1/drafts', draftBody);
  const createData = await createResp.json();

  if (createResp.status !== 200) {
    return { success: false, title, error: `Create failed: ${JSON.stringify(createData).slice(0, 200)}` };
  }

  let draftId = createData.id;

  // 2. Set slug
  await apiCall('PUT', `/api/v1/drafts/${draftId}`, { slug });

  // 3. Publish
  const publishResp = await apiCall('POST', `/api/v1/drafts/${draftId}/publish`);
  
  if (publishResp.status === 200) {
    return { success: true, title, slug, url: `https://engineeringforward.substack.com/p/${slug}` };
  } else {
    const publishData = await publishResp.json();
    return { success: false, title, error: `Publish failed: ${JSON.stringify(publishData).slice(0, 200)}` };
  }
}

(async () => {
  // Get all md files sorted oldest first (so they publish in chronological order)
  const files = fs.readdirSync(substackDir)
    .filter(f => f.endsWith('.md') && f !== 'latest.md' && !f.startsWith('publish'))
    .sort(); // oldest first

  // Already published slugs
  const published = new Set([
    'whats-important-now-the-10-programmer', 'whats-important-now-when-coding-became',
    'everywhere-and-nowhere', 'the-human-layer', 'when-the-interface-left-the-app',
    'recap-of-january-2026-the-end-of', 'the-new-engineering-job-is-to-make',
    'the-agent-stack-is-fragmentingand', 'the-agent-shift-is-an-infrastructure',
    'february-the-agent-stack-grows-up', 'what-the-review-becomes',
  ]);

  // Also check by title against published posts
  const publishedTitles = new Set([
    "What's important now - The 10% Programmer",
    "What's important now - When Coding Became Managing",
    'Everywhere and Nowhere',
    'The Human Layer',
    "When the Interface Left the App",
    'Recap of January 2026 : The end of coding: how AI agents are reshaping software engineering',
    'The new engineering job is to make systems legible to agents',
    'The agent stack is fragmenting—and that\u2019s good',
    'The agent shift is an infrastructure shift',
    'February : The agent stack grows up',
    'What the review becomes',
  ]);

  let published_count = 0;
  let failed_count = 0;
  let skipped_count = 0;

  for (const f of files) {
    const filepath = path.join(substackDir, f);
    const markdown = fs.readFileSync(filepath, 'utf-8');
    const title = markdown.match(/^# (.+)$/m)[1].trim();
    
    const slug = title.toLowerCase()
      .replace(/[^a-z0-9\s-]/g, '')
      .replace(/\s+/g, '-')
      .replace(/-+/g, '-')
      .replace(/^-|-$/g, '');

    if (published.has(slug) || publishedTitles.has(title)) {
      skipped_count++;
      continue;
    }

    // Skip v1 duplicates (keep v2)
    if (f.includes('when-code-becomes-cheap-engineering-becomes-expensive.md') && !f.includes('v2')) {
      skipped_count++;
      continue;
    }
    // Skip "What's important now" prefixed titles that are already published under different slugs
    if (title.startsWith("What's important now")) {
      skipped_count++;
      continue;
    }

    console.log(`\n[${published_count + failed_count + 1}] Publishing: ${title}`);
    
    try {
      const result = await publishPost(filepath);
      if (result.success) {
        console.log(`  ✅ ${result.url}`);
        published.add(slug);
        published_count++;
      } else {
        console.log(`  ❌ ${result.error}`);
        failed_count++;
      }
    } catch (e) {
      console.log(`  ❌ Exception: ${e.message}`);
      failed_count++;
    }

    // Small delay to avoid rate limiting
    await new Promise(r => setTimeout(r, 1000));
  }

  console.log(`\n\n=== SUMMARY ===`);
  console.log(`Published: ${published_count}`);
  console.log(`Failed: ${failed_count}`);
  console.log(`Skipped (already published): ${skipped_count}`);
})();