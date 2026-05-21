const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const pages = browser.contexts()[0].pages();
  let page = pages.find(p => p.url().includes('substack')) || pages[0];
  
  // Fresh draft
  await page.goto('https://engineeringforward.substack.com/publish/post/draft', { waitUntil: 'networkidle', timeout: 15000 });
  await sleep(6000);
  
  // Read markdown
  const mdContent = fs.readFileSync(path.join(__dirname, 'latest.md'), 'utf-8');
  const lines = mdContent.split('\n');
  const title = lines.find(l => l.startsWith('# '))?.replace(/^# /, '').trim() || '';
  
  // Build body JSON (same function)
  function buildJSON(lines) {
    let bodyStart = lines.findIndex(l => l.startsWith('# ')) + 1;
    if (bodyStart < lines.length && lines[bodyStart]?.trim() === '') bodyStart++;
    const content = [];
    for (let i = bodyStart; i < lines.length; i++) {
      const l = lines[i], t = l.trim();
      if (!t) continue;
      if (t.startsWith('*') && t.endsWith('*') && !t.startsWith('**')) {
        content.push({ type: 'paragraph', attrs: { textAlign: null }, content: [{ type: 'text', text: t.slice(1,-1).trim(), marks: [{ type: 'italic' }] }] });
        continue;
      }
      if (t.startsWith('### ')) { content.push({ type: 'heading', attrs: { level: 3 }, content: [{ type: 'text', text: t.slice(4).trim() }] }); continue; }
      if (t.startsWith('## ')) { content.push({ type: 'heading', attrs: { level: 2 }, content: [{ type: 'text', text: t.slice(3).trim() }] }); continue; }
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
        const li = remaining.indexOf('['), bi = remaining.indexOf('**');
        let ni = -1, nt = '';
        if (li !== -1) { ni = li; nt = 'link'; }
        if (bi !== -1 && (ni === -1 || bi < ni)) { ni = bi; nt = 'bold'; }
        if (ni === -1) { if (remaining) parts.push({ type: 'text', text: remaining }); break; }
        if (ni > 0) { parts.push({ type: 'text', text: remaining.slice(0, ni) }); remaining = remaining.slice(ni); }
        if (nt === 'link') {
          const close = remaining.indexOf(']('), end = remaining.indexOf(')', close+1);
          if (close !== -1 && end !== -1) {
            parts.push({ type: 'text', text: remaining.slice(1, close), marks: [{ type: 'link', attrs: { href: remaining.slice(close+2, end), target: '_blank', rel: 'noopener noreferrer nofollow', class: null } }] });
            remaining = remaining.slice(end+1);
          } else { parts.push({ type: 'text', text: remaining[0] }); remaining = remaining.slice(1); }
        } else {
          const end = remaining.indexOf('**', 2);
          if (end !== -1) { parts.push({ type: 'text', text: remaining.slice(2, end), marks: [{ type: 'bold' }] }); remaining = remaining.slice(end+2); }
          else { parts.push({ type: 'text', text: '**' }); remaining = remaining.slice(2); }
        }
      }
      content.push({ type: 'paragraph', attrs: { textAlign: null }, content: parts });
    }
    return { type: 'doc', content };
  }
  
  const json = buildJSON(lines);
  console.log(`Title: "${title}"`);
  console.log(`Body: ${json.content.length} blocks`);
  
  // STEP 1: Fill title textarea
  const titleTextarea = await page.$('textarea[placeholder="Title"]');
  if (titleTextarea) {
    await titleTextarea.click();
    await sleep(300);
    await titleTextarea.fill('');
    await sleep(100);
    await titleTextarea.type(title, { delay: 10 });
    console.log('Title filled.');
  } else {
    console.log('Title textarea not found!');
  }
  
  await sleep(500);
  
  // STEP 2: Inject body via TipTap
  const result = await page.evaluate(async (jsonData) => {
    const bodyEl = document.querySelector('[data-placeholder="Start writing..."]');
    if (!bodyEl?.editor) return 'no-editor';
    bodyEl.editor.commands.setContent(jsonData);
    bodyEl.editor.view.dom.dispatchEvent(new InputEvent('input', { bubbles: true, inputType: 'insertFromPaste' }));
    return bodyEl.editor.getJSON()?.content?.length || 0;
  }, json);
  console.log('Body blocks injected:', result);
  
  // STEP 3: Click into body and trigger a save
  await page.evaluate(() => {
    const bodyEl = document.querySelector('[data-placeholder="Start writing..."]');
    if (bodyEl) { bodyEl.focus(); bodyEl.click(); }
  });
  await sleep(500);
  await page.keyboard.press('ArrowRight');
  await page.keyboard.press('ArrowLeft');
  await sleep(500);
  
  // STEP 4: Click back on title to trigger title save
  if (titleTextarea) {
    await titleTextarea.click();
    await sleep(300);
  }
  
  console.log('Waiting for auto-save...');
  await sleep(10000);
  
  await page.screenshot({ path: path.join(__dirname, 'substack_draft_final.png'), fullPage: true });
  console.log('Screenshot saved.');
  console.log('URL:', page.url());
  fs.writeFileSync(path.join(__dirname, 'draft_url.txt'), page.url());
  console.log('Done!');
})();
