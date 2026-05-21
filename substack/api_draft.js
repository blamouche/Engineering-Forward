const fs = require('fs');
const path = require('path');

// Build the TipTap JSON content (same as before)
function buildJSON(lines) {
  let bodyStart = lines.findIndex(l => l.startsWith('# ')) + 1;
  if (bodyStart < lines.length && lines[bodyStart]?.trim() === '') bodyStart++;
  
  const content = [];
  for (let i = bodyStart; i < lines.length; i++) {
    const l = lines[i], t = l.trim();
    if (!t) continue;
    
    if (t.startsWith('*') && t.endsWith('*') && !t.startsWith('**')) {
      content.push({ type: 'paragraph', attrs: { textAlign: null }, content: [{ type: 'text', text: t.slice(1, -1).trim(), marks: [{ type: 'italic' }] }] });
      continue;
    }
    if (t.startsWith('### ')) {
      content.push({ type: 'heading', attrs: { level: 3 }, content: [{ type: 'text', text: t.slice(4).trim() }] });
      continue;
    }
    if (t.startsWith('## ')) {
      content.push({ type: 'heading', attrs: { level: 2 }, content: [{ type: 'text', text: t.slice(3).trim() }] });
      continue;
    }
    if (t === '---') { content.push({ type: 'horizontalRule' }); continue; }
    
    const sm = t.match(/^(\d+\.)\s+\[(.*?)\]\((.*?)\)$/);
    if (sm) {
      content.push({ type: 'paragraph', attrs: { textAlign: null }, content: [
        { type: 'text', text: sm[1] + ' ' },
        { type: 'text', text: sm[2], marks: [{ type: 'link', attrs: { href: sm[3], target: '_blank', rel: 'noopener noreferrer nofollow', class: null } }] }
      ]});
      continue;
    }
    
    const parts = [];
    let remaining = l;
    while (remaining.length > 0) {
      const li = remaining.indexOf('[');
      const bi = remaining.indexOf('**');
      let ni = -1, nt = '';
      if (li !== -1) { ni = li; nt = 'link'; }
      if (bi !== -1 && (ni === -1 || bi < ni)) { ni = bi; nt = 'bold'; }
      
      if (ni === -1) {
        if (remaining) parts.push({ type: 'text', text: remaining });
        break;
      }
      if (ni > 0) { parts.push({ type: 'text', text: remaining.slice(0, ni) }); remaining = remaining.slice(ni); }
      
      if (nt === 'link') {
        const close = remaining.indexOf(']('), end = remaining.indexOf(')', close + 1);
        if (close !== -1 && end !== -1) {
          parts.push({ type: 'text', text: remaining.slice(1, close), marks: [{ type: 'link', attrs: { href: remaining.slice(close+2, end), target: '_blank', rel: 'noopener noreferrer nofollow', class: null } }] });
          remaining = remaining.slice(end+1);
        } else { parts.push({ type: 'text', text: remaining[0] }); remaining = remaining.slice(1); }
      } else {
        const end = remaining.indexOf('**', 2);
        if (end !== -1) {
          parts.push({ type: 'text', text: remaining.slice(2, end), marks: [{ type: 'bold' }] });
          remaining = remaining.slice(end+2);
        } else { parts.push({ type: 'text', text: '**' }); remaining = remaining.slice(2); }
      }
    }
    content.push({ type: 'paragraph', attrs: { textAlign: null }, content: parts });
  }
  return { type: 'doc', content };
}

const md = fs.readFileSync(path.join(__dirname, 'latest.md'), 'utf-8');
const lines = md.split('\n');
const title = lines.find(l => l.startsWith('# '))?.replace(/^# /, '').trim() || '';

const bodyJSON = buildJSON(lines);
console.log('Blocks:', bodyJSON.content.length);

// Now use the Substack API directly with cookies
const cookies = JSON.parse(fs.readFileSync(path.join(__dirname, 'substack_cookies.json'), 'utf-8'));
console.log('Auth cookies available:', Object.keys(cookies).filter(k => k.includes('sid') || k.includes('lli')));

// Build cookie header
const cookieHeader = Object.entries(cookies)
  .map(([k, v]) => `${k}=${v}`)
  .join('; ');

const BASE = 'https://engineeringforward.substack.com';

async function apiCall(method, path, body = null) {
  const opts = {
    method,
    headers: {
      'Cookie': cookieHeader,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
      'Referer': BASE,
    }
  };
  if (body) opts.body = JSON.stringify(body);
  
  const resp = await fetch(`${BASE}${path}`, opts);
  const text = await resp.text();
  let data;
  try { data = JSON.parse(text); } catch(e) { data = text; }
  return { status: resp.status, data };
}

(async () => {
  // 1. Get drafts to find a reference draft (needed to copy structure)
  console.log('\n1. Getting drafts...');
  const draftsResp = await apiCall('GET', '/api/v1/drafts');
  console.log('Status:', draftsResp.status);
  
  if (!Array.isArray(draftsResp.data)) {
    console.log('Response:', JSON.stringify(draftsResp.data).slice(0, 300));
    console.log('Authentication may have failed. Cookies might be expired.');
    // Try getting the user info first
    const meResp = await apiCall('GET', '/api/v1/me');
    console.log('Me endpoint:', meResp.status, JSON.stringify(meResp.data).slice(0, 200));
    process.exit(1);
  }
  
  const drafts = draftsResp.data;
  console.log('Found', drafts.length, 'drafts');
  
  // Find an unpublished draft to use as template
  const templateDraft = drafts.find(d => !d.is_published) || drafts[0];
  if (!templateDraft) {
    console.log('No drafts found! Need at least one existing draft.');
    process.exit(1);
  }
  console.log('Template draft:', templateDraft.id, templateDraft.title?.slice(0, 50));
  
  // 2. Get the template draft's full data
  console.log('\n2. Getting template draft structure...');
  const templateResp = await apiCall('GET', `/api/v1/drafts/${templateDraft.id}`);
  console.log('Status:', templateResp.status);
  
  if (templateResp.status !== 200) {
    console.log('Failed to get template draft');
    process.exit(1);
  }
  
  const template = templateResp.data;
  console.log('Template keys:', Object.keys(template).join(', '));
  
  // 3. Create a new draft based on the template
  console.log('\n3. Creating new draft...');
  
  const newDraft = {
    ...template,
    id: undefined,
    draft_id: undefined,
    title: title,
    subtitle: '',
    body_json: JSON.stringify(bodyJSON),
    body_text: '', // will be regenerated
    audience: 'everyone',
    type: 'newsletter',
    section_id: null,
    podcast_episode_id: null,
    video_upload_id: null,
    write_comment_permissions: 'everyone',
    email_markdown: null,
    should_send_email: false,
    is_published: false,
    published_at: null,
    created_at: null,
    updated_at: null,
    word_count: null,
  };
  
  // Remove fields that shouldn't be sent
  delete newDraft.id;
  delete newDraft.draft_id;
  delete newDraft.created_at;
  delete newDraft.updated_at;
  delete newDraft.published_at;
  delete newDraft.published_date;
  delete newDraft.word_count;
  
  const createResp = await apiCall('POST', '/api/v1/drafts', newDraft);
  console.log('Create status:', createResp.status);
  
  if (createResp.status === 200 || createResp.status === 201) {
    const created = createResp.data;
    console.log('Draft created!');
    console.log('Draft ID:', created.id || created.draft_id);
    console.log('Draft URL:', `${BASE}/publish/post/draft/${created.id || created.draft_id || ''}`);
  } else {
    console.log('Response:', JSON.stringify(createResp.data).slice(0, 500));
    
    // Try alternative: update an existing draft
    console.log('\nTrying to update template draft instead...');
    const updateBody = {
      ...template,
      title: title,
      body_json: JSON.stringify(bodyJSON),
    };
    const updateResp = await apiCall('PUT', `/api/v1/drafts/${templateDraft.id}`, updateBody);
    console.log('Update status:', updateResp.status);
    if (updateResp.status === 200) {
      console.log('Draft updated! URL:', `${BASE}/publish/post/draft`);
    }
  }
})();
