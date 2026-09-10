const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, 'latest.md');
const markdown = fs.readFileSync(file, 'utf-8');
const title = markdown.match(/^# (.+)$/m)[1].trim();
const subtitleMatch = markdown.match(/^\*(.+)\*$/m);
const subtitle = subtitleMatch ? subtitleMatch[1].trim() : '';

// Extract body (between subtitle and ---)
const lines = markdown.split('\n');
let bodyStart = 0;
let bodyEnd = lines.length;
for (let i = 0; i < lines.length; i++) {
  if (lines[i].match(/^\*(.+)\*$/)) { bodyStart = i + 1; break; }
}
for (let i = bodyStart; i < lines.length; i++) {
  if (lines[i].trim() === '---') { bodyEnd = i; break; }
}
let bodyLines = lines.slice(bodyStart, bodyEnd).join('\n').trim();

// Build body JSON for Substack API
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

const bodyJSON = buildJSON(bodyLines);
console.log('Title:', title);
console.log('Subtitle:', subtitle);
console.log('Body blocks:', bodyJSON.content.length);

const cookies = JSON.parse(fs.readFileSync(path.join(__dirname, 'substack_cookies.json'), 'utf-8'));
const cookieStr = Object.entries(cookies).map(([k,v]) => `${k}=${v}`).join('; ');
const BASE = 'https://engineeringforward.substack.com';

async function apiCall(method, url, body) {
  const opts = { method, headers: { 'Cookie': cookieStr, 'Content-Type': 'application/json' } };
  if (body) opts.body = JSON.stringify(body);
  const resp = await fetch(BASE + url, opts);
  return resp;
}

(async () => {
  // Generate slug
  const slug = title.toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');

  // 1. Create draft
  console.log('\n1. Creating draft...');
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
  console.log('Create status:', createResp.status);

  let draftId;
  if (createResp.status === 200) {
    draftId = createData.id;
    console.log('Draft created! ID:', draftId);
  } else {
    console.log('Error:', JSON.stringify(createData).slice(0, 500));
    process.exit(1);
  }

  // 2. Update slug
  console.log('\n2. Setting slug...');
  const updateResp = await apiCall('PUT', `/api/v1/drafts/${draftId}`, { slug });
  console.log('Update status:', updateResp.status);

  // 3. Publish
  console.log('\n3. Publishing draft', draftId, '...');
  const publishResp = await apiCall('POST', `/api/v1/drafts/${draftId}/publish`);
  const publishData = await publishResp.json();
  console.log('Publish status:', publishResp.status);

  if (publishResp.status === 200) {
    console.log('\n✅ SUCCESS: Post published!');
    console.log('URL: https://engineeringforward.substack.com/p/' + slug);
  } else {
    console.log('Publish response:', JSON.stringify(publishData).slice(0, 500));
  }
})();