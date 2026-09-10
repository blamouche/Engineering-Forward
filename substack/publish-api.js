const fs = require('fs');
const path = require('path');

// Read the markdown file
const file = path.join(__dirname, '20260909-post-what-the-review-becomes.md');
const markdown = fs.readFileSync(file, 'utf-8');

// Extract title
const title = markdown.match(/^# (.+)$/m)[1].trim();

// Extract subtitle
const subtitleMatch = markdown.match(/^\*(.+)\*$/m);
const subtitle = subtitleMatch ? subtitleMatch[1].trim() : '';

// Extract body (between subtitle and ---)
const bodyStart = markdown.indexOf('*', markdown.indexOf('\n') + 1);
const bodyEnd = markdown.indexOf('\n---\n', bodyStart);
let body = markdown.substring(bodyStart, bodyEnd).replace(/^\*.+\*\n+/, '').trim();

// Extract sources section
const sourcesStart = markdown.indexOf('## Sources');
const sourcesText = markdown.substring(sourcesStart);

// Build TipTap JSON content from the body
function buildJSON(md) {
  const lines = md.split('\n');
  const content = [];
  
  for (let i = 0; i < lines.length; i++) {
    const l = lines[i];
    const t = l.trim();
    if (!t) continue;
    
    // Subheadings (## )
    if (t.startsWith('## ')) {
      content.push({ 
        type: 'heading', 
        attrs: { level: 2 }, 
        content: [{ type: 'text', text: t.slice(3).trim() }] 
      });
      continue;
    }
    
    // Horizontal rule
    if (t === '---') { 
      content.push({ type: 'horizontalRule' }); 
      continue; 
    }
    
    // Sources heading
    if (t.startsWith('## Sources')) {
      content.push({ type: 'heading', attrs: { level: 2 }, content: [{ type: 'text', text: 'Sources' }] });
      continue;
    }
    
    // Numbered list items (sources): "1. [Title](url)"
    const numMatch = t.match(/^(\d+)\.\s+\[(.*?)\]\((.*?)\)$/);
    if (numMatch) {
      content.push({ 
        type: 'paragraph', 
        attrs: { textAlign: null }, 
        content: [
          { type: 'text', text: numMatch[1] + '. ' },
          { type: 'text', text: numMatch[2], marks: [{ type: 'link', attrs: { href: numMatch[3], target: '_blank', rel: 'noopener noreferrer nofollow', class: null } }] }
        ]
      });
      continue;
    }
    
    // Regular paragraph with possible links and bold
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
      if (ni > 0) { 
        parts.push({ type: 'text', text: remaining.slice(0, ni) }); 
        remaining = remaining.slice(ni); 
      }
      
      if (nt === 'link') {
        const close = remaining.indexOf('](');
        const end = remaining.indexOf(')', close + 1);
        if (close !== -1 && end !== -1) {
          parts.push({ 
            type: 'text', 
            text: remaining.slice(1, close), 
            marks: [{ type: 'link', attrs: { href: remaining.slice(close+2, end), target: '_blank', rel: 'noopener noreferrer nofollow', class: null } }] 
          });
          remaining = remaining.slice(end+1);
        } else { 
          parts.push({ type: 'text', text: remaining[0] }); 
          remaining = remaining.slice(1); 
        }
      } else {
        const end = remaining.indexOf('**', 2);
        if (end !== -1) {
          parts.push({ type: 'text', text: remaining.slice(2, end), marks: [{ type: 'bold' }] });
          remaining = remaining.slice(end+2);
        } else { 
          parts.push({ type: 'text', text: '**' }); 
          remaining = remaining.slice(2); 
        }
      }
    }
    content.push({ type: 'paragraph', attrs: { textAlign: null }, content: parts });
  }
  return { type: 'doc', content };
}

// Include sources in the body
const fullBody = body + '\n\n---\n\n' + sourcesText;
const bodyJSON = buildJSON(fullBody);
console.log('Title:', title);
console.log('Subtitle:', subtitle);
console.log('Body blocks:', bodyJSON.content.length);

// Load cookies
const cookies = JSON.parse(fs.readFileSync(path.join(__dirname, 'substack_cookies.json'), 'utf-8'));
const cookieHeader = Object.entries(cookies).map(([k,v]) => `${k}=${v}`).join('; ');
const BASE = 'https://engineeringforward.substack.com';

async function apiCall(method, url, body = null) {
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
  
  const resp = await fetch(url, opts);
  const text = await resp.text();
  let data;
  try { data = JSON.parse(text); } catch(e) { data = text; }
  return { status: resp.status, data };
}

(async () => {
  // 1. Get existing drafts to use as template
  console.log('\n1. Getting drafts...');
  const draftsResp = await apiCall('GET', `${BASE}/api/v1/drafts`);
  console.log('Status:', draftsResp.status);
  
  if (draftsResp.status !== 200 || !draftsResp.data.posts) {
    console.log('Failed to get drafts:', JSON.stringify(draftsResp.data).slice(0, 200));
    process.exit(1);
  }
  
  const posts = draftsResp.data.posts;
  console.log('Found', posts.length, 'posts');
  
  // Find an unpublished draft or use the most recent post as template
  let template = posts.find(p => !p.is_published);
  if (!template) {
    console.log('No unpublished drafts. Using most recent post as template...');
    template = posts[0];
  }
  
  const draftId = template.id;
  console.log('Template draft ID:', draftId, 'Title:', template.title?.slice(0, 50));
  
  // 2. Get the full template draft
  console.log('\n2. Getting template draft details...');
  const templateResp = await apiCall('GET', `${BASE}/api/v1/drafts/${draftId}`);
  console.log('Status:', templateResp.status);
  
  if (templateResp.status !== 200) {
    console.log('Failed:', JSON.stringify(templateResp.data).slice(0, 200));
    process.exit(1);
  }
  
  const tpl = templateResp.data;
  console.log('Template keys:', Object.keys(tpl).join(', ').slice(0, 200));
  
  // 3. Create new draft
  console.log('\n3. Creating new draft...');
  const newDraft = {
    draft_title: title,
    subtitle: subtitle,
    body_json: JSON.stringify(bodyJSON),
    body: JSON.stringify(bodyJSON), // Some endpoints use body
    type: 'newsletter',
    audience: 'everyone',
    section_id: null,
    podcast_episode_id: null,
    video_upload_id: null,
    write_comment_permissions: 'everyone',
    email_markdown: null,
    should_send_email: true,
    is_published: false,
    draft_settings: {
      ...tpl.draft_settings,
      send_preview_email: false,
    },
  };
  
  const createResp = await apiCall('POST', `${BASE}/api/v1/drafts`, newDraft);
  console.log('Create status:', createResp.status);
  
  let newDraftId;
  if (createResp.status === 200 || createResp.status === 201) {
    const created = createResp.data;
    newDraftId = created.id || created.draft_id;
    console.log('Draft created! ID:', newDraftId);
  } else {
    console.log('Create response:', JSON.stringify(createResp.data).slice(0, 500));
    
    // Try updating the template draft instead
    console.log('\nTrying to update existing draft...');
    const updateBody = {
      ...tpl,
      draft_title: title,
      title: title,
      subtitle: subtitle,
      body_json: JSON.stringify(bodyJSON),
    };
    delete updateBody.is_published;
    delete updateBody.post_date;
    delete updateBody.email_sent_at;
    
    const updateResp = await apiCall('PUT', `${BASE}/api/v1/drafts/${draftId}`, updateBody);
    console.log('Update status:', updateResp.status);
    console.log('Update response:', JSON.stringify(updateResp.data).slice(0, 300));
    
    if (updateResp.status === 200) {
      newDraftId = draftId;
      console.log('Draft updated! ID:', newDraftId);
    } else {
      process.exit(1);
    }
  }
  
  // 4. Publish the draft
  console.log('\n4. Publishing draft', newDraftId, '...');
  const publishResp = await apiCall('POST', `${BASE}/api/v1/drafts/${newDraftId}/publish`);
  console.log('Publish status:', publishResp.status);
  console.log('Publish response:', JSON.stringify(publishResp.data).slice(0, 500));
  
  if (publishResp.status === 200) {
    const slug = 'what-the-review-becomes';
    console.log('\nSUCCESS: Post published!');
    console.log('URL: https://engineeringforward.substack.com/p/' + slug);
  } else {
    // Try alternative publish endpoint
    console.log('\nTrying alternative publish endpoint...');
    const altPublish = await apiCall('POST', `${BASE}/api/v1/posts`, { 
      draft_id: newDraftId,
      is_published: true,
      audience: 'everyone',
    });
    console.log('Alt publish status:', altPublish.status);
    console.log('Alt publish response:', JSON.stringify(altPublish.data).slice(0, 300));
  }
})();