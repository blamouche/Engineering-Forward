const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ARTICLE_FILE = path.join(__dirname, 'substack', '20260926-post-the-reporting-line.md');
const markdown = fs.readFileSync(ARTICLE_FILE, 'utf-8');

const lines = markdown.split('\n');
const title = lines[0].replace(/^# /, '');
let subtitle = '';
let bodyStart = 0;
for (let i = 1; i < lines.length; i++) {
  if (lines[i].trim() === '') continue;
  if (lines[i].startsWith('*') && lines[i].endsWith('*')) {
    subtitle = lines[i].replace(/^\*/, '').replace(/\*$/, '').trim();
    bodyStart = i + 1;
    break;
  }
}

let body = '';
for (let i = bodyStart; i < lines.length; i++) {
  if (lines[i].trim() === '---') break;
  body += lines[i] + '\n';
}

function markdownToHtml(md) {
  let html = '';
  let inList = false;
  const mdLines = md.split('\n');
  for (let i = 0; i < mdLines.length; i++) {
    let line = mdLines[i];
    if (line.trim() === '') {
      if (inList) { html += '</ul>\n'; inList = false; }
      continue;
    }
    if (line.startsWith('## ')) {
      if (inList) { html += '</ul>\n'; inList = false; }
      html += '<h2>' + convertInline(line.replace(/^## /, '')) + '</h2>\n';
      continue;
    }
    if (line.startsWith('# ')) {
      if (inList) { html += '</ul>\n'; inList = false; }
      html += '<h1>' + convertInline(line.replace(/^# /, '')) + '</h1>\n';
      continue;
    }
    if (line.startsWith('- ')) {
      if (!inList) { html += '<ul>\n'; inList = true; }
      html += '<li>' + convertInline(line.replace(/^- /, '')) + '</li>\n';
      continue;
    }
    if (inList) { html += '</ul>\n'; inList = false; }
    html += '<p>' + convertInline(line) + '</p>\n';
  }
  if (inList) html += '</ul>\n';
  return html;
}

function convertInline(text) {
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
  text = text.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  text = text.replace(/\*([^*]+)\*/g, '<em>$1</em>');
  return text;
}

const htmlBody = markdownToHtml(body);
console.log('Title:', title);
console.log('Subtitle:', subtitle);
console.log('Body HTML length:', htmlBody.length);

(async () => {
  // Read the DevToolsActivePort file to get the ws endpoint
  const activePortFile = process.env.HOME + '/Library/Application Support/Google/Chrome/DevToolsActivePort';
  const portContent = fs.readFileSync(activePortFile, 'utf-8').trim();
  const [port, wsPath] = portContent.split('\n');
  const wsUrl = `ws://localhost:${port}${wsPath}`;
  console.log('WebSocket URL:', wsUrl);
  
  console.log('Connecting to running Chrome...');
  
  const browser = await chromium.connectOverCDP(wsUrl);
  console.log('Connected!');
  
  const contexts = browser.contexts();
  console.log('Number of contexts:', contexts.length);
  
  let context;
  if (contexts.length > 0) {
    context = contexts[0];
    console.log('Using existing context');
  } else {
    console.log('No existing context, creating new one');
    context = await browser.newContext();
  }
  
  const page = await context.newPage();
  page.setDefaultTimeout(30000);
  
  try {
    console.log('Navigating to Substack publish page...');
    await page.goto('https://engineeringforward.substack.com/publish/post', { waitUntil: 'networkidle' });
    await page.waitForTimeout(5000);
    
    const currentUrl = page.url();
    console.log('Current URL:', currentUrl);
    
    if (currentUrl.includes('sign-in')) {
      console.log('NOT_LOGGED_IN');
      await page.screenshot({ path: '/tmp/substack-signin.png' });
      await page.close();
      browser.close();
      process.exit(2);
    }
    
    // Wait for title field
    await page.waitForSelector('textarea.pencraft.page-title', { timeout: 10000 });
    
    console.log('Editor found! Filling title...');
    await page.evaluate((t) => {
      const el = document.querySelector('textarea.pencraft.page-title');
      el.value = t;
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    }, title);
    await page.waitForTimeout(1000);
    
    console.log('Filling subtitle...');
    await page.evaluate((s) => {
      const el = document.querySelector('textarea.pencraft.subtitle');
      if (el) {
        el.value = s;
        el.dispatchEvent(new Event('input', { bubbles: true }));
        el.dispatchEvent(new Event('change', { bubbles: true }));
      }
    }, subtitle);
    await page.waitForTimeout(1000);
    
    console.log('Inserting body...');
    await page.evaluate((html) => {
      const editor = document.querySelector('.tiptap.ProseMirror') || document.querySelector('[contenteditable="true"]');
      if (editor) {
        editor.focus();
        document.execCommand('selectAll', false, null);
        document.execCommand('insertHTML', false, html);
      }
    }, htmlBody);
    
    console.log('Waiting for save...');
    await page.waitForTimeout(5000);
    await page.screenshot({ path: '/tmp/substack-filled.png' });
    
    console.log('Looking for Continue button...');
    const continueClicked = await page.evaluate(() => {
      const buttons = Array.from(document.querySelectorAll('button'));
      const btn = buttons.find(b => b.textContent.includes('Continuer') || b.textContent.includes('Continue'));
      if (btn) { btn.click(); return true; }
      return false;
    });
    
    if (continueClicked) console.log('Clicked Continue');
    else {
      const buttons = await page.$$eval('button', btns => btns.map(b => b.textContent.slice(0, 50)));
      console.log('Available buttons:', buttons);
    }
    
    await page.waitForTimeout(5000);
    await page.screenshot({ path: '/tmp/substack-publish.png' });
    
    console.log('Looking for publish button...');
    const publishClicked = await page.evaluate(() => {
      const buttons = Array.from(document.querySelectorAll('button'));
      const btn = buttons.find(b => 
        b.textContent.includes('Envoyer à tous') || b.textContent.includes('Send to everyone') ||
        b.textContent.includes('Publish now') || b.textContent.includes('Publier maintenant')
      );
      if (btn) { btn.click(); return true; }
      return false;
    });
    
    if (publishClicked) {
      console.log('Clicked publish button');
      await page.waitForTimeout(3000);
      
      const noBtnClicked = await page.evaluate(() => {
        const buttons = Array.from(document.querySelectorAll('button'));
        const btn = buttons.find(b => 
          b.textContent.includes('Publier sans boutons') || b.textContent.includes('Publish without buttons') ||
          b.textContent.includes('sans boutons')
        );
        if (btn) { btn.click(); return true; }
        return false;
      });
      if (noBtnClicked) console.log('Clicked "Publish without buttons"');
    }
    
    await page.waitForTimeout(5000);
    await page.screenshot({ path: '/tmp/substack-published.png' });
    const finalUrl = page.url();
    console.log('Final URL:', finalUrl);
    
    if (finalUrl.includes('/publish/posts/detail/') || finalUrl.includes('/p/')) {
      console.log('SUCCESS: Post published');
      console.log('PUBLISHED_URL:' + finalUrl);
    } else {
      console.log('UNCERTAIN');
      console.log('FINAL_URL:' + finalUrl);
    }
    
  } catch (err) {
    console.error('ERROR:', err.message);
    await page.screenshot({ path: '/tmp/substack-error.png' }).catch(() => {});
  }
  
  await page.close();
  browser.close();
})();