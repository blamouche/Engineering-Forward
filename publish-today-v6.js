const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const ARTICLE_FILE = path.join(__dirname, 'substack', '20260929-post-the-agents-that-eat-the-walls.md');
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

// Load all cookies from auth file
const authCookies = JSON.parse(fs.readFileSync('/Users/openclaw/.substack-auth.json', 'utf-8'));
// Also load old cookies
const oldCookies = JSON.parse(fs.readFileSync('/tmp/substack-cookies-clean.json', 'utf-8'));

(async () => {
  console.log('Launching Chrome with fresh temp profile + cookie injection...');
  
  const browser = await puppeteer.launch({
    headless: false,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    userDataDir: '/tmp/chrome-substack-fresh-' + Date.now(),
    args: ['--no-first-run', '--no-default-browser-check', '--disable-extensions'],
    defaultViewport: { width: 1280, height: 900 }
  });
  
  const page = await browser.newPage();
  page.setDefaultTimeout(30000);
  
  // Set User-Agent to match a real browser
  await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36');
  
  // First navigate to substack.com to establish the domain
  console.log('Navigating to substack.com...');
  await page.goto('https://substack.com', { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 3000));
  
  // Inject cookies - try both sets
  console.log('Injecting cookies...');
  const allCookies = [...oldCookies, ...authCookies];
  for (const c of allCookies) {
    try {
      // Only set cookies for substack domains
      if (c.domain && c.domain.includes('substack')) {
        await page.setCookie({
          name: c.name,
          value: String(c.value),
          domain: c.domain,
          path: c.path || '/',
          httpOnly: c.httpOnly,
          secure: c.secure,
          sameSite: c.sameSite || 'None',
          expires: c.expires > 0 ? c.expires : undefined
        });
      }
    } catch (e) {
      // skip invalid cookies
    }
  }
  console.log('Cookies injected');
  
  // Now navigate to the publish page
  console.log('Navigating to Substack publish page...');
  await page.goto('https://engineeringforward.substack.com/publish/post', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 5000));
  
  const currentUrl = page.url();
  console.log('Current URL:', currentUrl);
  
  if (currentUrl.includes('sign-in')) {
    console.log('NOT_LOGGED_IN - session cookies are expired');
    await page.screenshot({ path: '/tmp/substack-signin-fresh.png' });
    await browser.close();
    process.exit(2);
  }
  
  let titleEl = await page.$('textarea.pencraft.page-title');
  if (!titleEl) {
    await new Promise(r => setTimeout(r, 5000));
    titleEl = await page.$('textarea.pencraft.page-title');
  }
  
  if (!titleEl) {
    console.log('EDITOR_NOT_FOUND');
    await page.screenshot({ path: '/tmp/substack-editor-fresh.png' });
    await browser.close();
    process.exit(3);
  }
  
  console.log('Editor found! Filling title...');
  await page.evaluate((t) => {
    const el = document.querySelector('textarea.pencraft.page-title');
    el.value = t;
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
  }, title);
  await new Promise(r => setTimeout(r, 1000));
  
  console.log('Filling subtitle...');
  await page.evaluate((s) => {
    const el = document.querySelector('textarea.pencraft.subtitle');
    if (el) {
      el.value = s;
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }, subtitle);
  await new Promise(r => setTimeout(r, 1000));
  
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
  await new Promise(r => setTimeout(r, 5000));
  await page.screenshot({ path: '/tmp/substack-filled-fresh.png' });
  
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
  
  await new Promise(r => setTimeout(r, 5000));
  await page.screenshot({ path: '/tmp/substack-publish-fresh.png' });
  
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
    await new Promise(r => setTimeout(r, 3000));
    
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
  
  await new Promise(r => setTimeout(r, 5000));
  await page.screenshot({ path: '/tmp/substack-published-fresh.png' });
  const finalUrl = page.url();
  console.log('Final URL:', finalUrl);
  
  if (finalUrl.includes('/publish/posts/detail/') || finalUrl.includes('/p/')) {
    console.log('SUCCESS: Post published');
    console.log('PUBLISHED_URL:' + finalUrl);
  } else {
    console.log('UNCERTAIN');
    console.log('FINAL_URL:' + finalUrl);
  }
  
  await browser.close();
})();