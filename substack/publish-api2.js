const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, '20260909-post-what-the-review-becomes.md');
const markdown = fs.readFileSync(file, 'utf-8');
const title = markdown.match(/^# (.+)$/m)[1].trim();
const subtitleMatch = markdown.match(/^\*(.+)\*$/m);
const subtitle = subtitleMatch ? subtitleMatch[1].trim() : '';

const bodyStart = markdown.indexOf('*', markdown.indexOf('\n') + 1);
const bodyEnd = markdown.indexOf('\n---\n', bodyStart);
let body = markdown.substring(bodyStart, bodyEnd).replace(/^\*.+\*\n+/, '').trim();
const sourcesStart = markdown.indexOf('## Sources');
const sourcesText = markdown.substring(sourcesStart);

function buildJSON(md) {
  const lines = md.split('\n');
  const content = [];
  for (let i = 0; i < lines.length; i++) {
    const l = lines[i];
    const t = l.trim();
    if (!t) continue;
    if (t.startsWith('## ')) {
      content.push({ type: 'heading', attrs: { level: 2 }, content: [{ type: 'text', text: t.slice(3).trim() }] });
      continue;
    }
    if (t === '---') { content.push({ type: 'horizontalRule' }); continue; }
    const numMatch = t.match(/^(\d+)\.\s+\[(.*?)\]\((.*?)\)$/);
    if (numMatch) {
      content.push({ type: 'paragraph', attrs: { textAlign: null }, content: [
        { type: 'text', text: numMatch[1] + '. ' },
        { type: 'text', text: numMatch[2], marks: [{ type: 'link', attrs: { href: numMatch[3], target: '_blank', rel: 'noopener noreferrer nofollow', class: null } }] }
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
      if (ni === -1) { if (remaining) parts.push({ type: 'text', text: remaining }); break; }
      if (ni > 0) { parts.push({ type: 'text', text: remaining.slice(0, ni) }); remaining = remaining.slice(ni); }
      if (nt === 'link') {
        const close = remaining.indexOf('](');
        const end = remaining.indexOf(')', close + 1);
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

const fullBody = body + '\n\n---\n\n' + sourcesText;
const bodyJSON = buildJSON(fullBody);
const bodyJSONStr = JSON.stringify(bodyJSON);
console.log('Title:', title);
console.log('Subtitle:', subtitle);
console.log('Body blocks:', bodyJSON.content.length);

const cookies = JSON.parse(fs.readFileSync(path.join(__dirname, 'substack_cookies.json'), 'utf-8'));
const cookieHeader = Object.entries(cookies).map(([k,v]) => `${k}=${v}`).join('; ');
const BASE = 'https://engineeringforward.substack.com';

async function apiCall(method, urlPath, body = null) {
  const opts = { method, headers: { 'Cookie': cookieHeader, 'Content-Type': 'application/json' } };
  if (body) opts.body = JSON.stringify(body);
  const resp = await fetch(`${BASE}${urlPath}`, opts);
  const text = await resp.text();
  let data; try { data = JSON.parse(text); } catch(e) { data = text; }
  return { status: resp.status, data };
}

(async () => {
  // 1. Get template draft
  console.log('\n1. Getting drafts...');
  const draftsResp = await apiCall('GET', '/api/v1/drafts');
  if (draftsResp.status !== 200) { console.log('Failed:', draftsResp.status); process.exit(1); }
  const posts = draftsResp.data.posts;
  const template = posts.find(p => !p.is_published) || posts[0];
  const draftId = template.id;
  console.log('Template:', draftId, template.title?.slice(0, 50));
  
  // 2. Get full template
  const tplResp = await apiCall('GET', `/api/v1/drafts/${draftId}`);
  if (tplResp.status !== 200) { console.log('Failed to get template'); process.exit(1); }
  const tpl = tplResp.data;
  
  // 3. Create new draft with proper structure
  console.log('\n2. Creating new draft...');
  const newDraft = {
    draft_title: title,
    draft_subtitle: subtitle,
    title: title,
    subtitle: subtitle,
    body: bodyJSONStr,
    draft_body: bodyJSONStr,
    type: 'newsletter',
    audience: 'everyone',
    draft_section_id: null,
    section_id: null,
    should_send_email: true,
    should_send_free_preview: false,
    show_guest_bios: true,
    write_comment_permissions: 'everyone',
    is_draft_hidden: false,
    has_dismissed_tk_warning: true,
    meter_type: 'none',
    account_based_meter_type: 'metered',
    slug: 'what-the-review-becomes',
    language: 'en',
    ai_detection_disabled: false,
    editor_v2: false,
    draft_bylines: tpl.postBylines || [],
    pending_invites: [],
    cover_image: null,
    podcast_art_url: null,
    description: null,
    search_engine_description: null,
    search_engine_title: null,
    social_title: null,
    free_unlock_required: false,
    syndicate_voiceover_to_rss: false,
    exempt_from_archive_paywall: false,
    teaser_post_eligible: true,
    explicit: null,
    default_comment_sort: null,
    hide_from_feed: false,
    email_from_name: null,
  };
  
  const createResp = await apiCall('POST', '/api/v1/drafts', newDraft);
  console.log('Create status:', createResp.status);
  
  let newDraftId;
  if (createResp.status === 200 || createResp.status === 201) {
    newDraftId = createResp.data.id || createResp.data.draft_id;
    console.log('Draft created! ID:', newDraftId);
  } else {
    console.log('Create failed:', JSON.stringify(createResp.data).slice(0, 500));
    
    // Try without draft_bylines
    console.log('\nTrying without draft_bylines...');
    const draft2 = { ...newDraft };
    delete draft2.draft_bylines;
    delete draft2.pending_invites;
    const createResp2 = await apiCall('POST', '/api/v1/drafts', draft2);
    console.log('Status:', createResp2.status);
    console.log('Response:', JSON.stringify(createResp2.data).slice(0, 500));
    
    if (createResp2.status === 200 || createResp2.status === 201) {
      newDraftId = createResp2.data.id || createResp2.data.draft_id;
      console.log('Draft created! ID:', newDraftId);
    } else {
      process.exit(1);
    }
  }
  
  // 4. Publish
  console.log('\n3. Publishing draft', newDraftId, '...');
  const publishResp = await apiCall('POST', `/api/v1/drafts/${newDraftId}/publish`);
  console.log('Publish status:', publishResp.status);
  console.log('Publish response:', JSON.stringify(publishResp.data).slice(0, 500));
  
  if (publishResp.status === 200) {
    console.log('\nSUCCESS: Post published!');
    console.log('URL: https://engineeringforward.substack.com/p/what-the-review-becomes');
  } else {
    // Try with body
    console.log('\nTrying publish with body...');
    const pubBody = { audience: 'everyone', should_send_email: true };
    const pubResp2 = await apiCall('POST', `/api/v1/drafts/${newDraftId}/publish`, pubBody);
    console.log('Status:', pubResp2.status);
    console.log('Response:', JSON.stringify(pubResp2.data).slice(0, 500));
  }
})();