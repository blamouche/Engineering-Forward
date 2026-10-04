const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const ARTICLE_FILE = path.join(__dirname, 'substack', '20260922-post-the-one-way-door.md');
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

(async () => {
  // Try the Default/Default profile (the path structure shows Default/Default/Cookies)
  // The userDataDir should be: ~/Library/Application Support/Google/Chrome/Default
  // and profile-directory = Default
  const userDataDir = process.env.HOME + '/Library/Application Support/Google/Chrome/Default';
  
  console.log('Using userDataDir:', userDataDir);
  
  const browser = await puppeteer.launch({
    headless: false,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    userDataDir: userDataDir,
    args: ['--no-first-run', '--no-default-browser-check', '--disable-extensions', '--profile-directory=Default'],
    defaultViewport: { width: 1280, height: 900 }
  });
  
  const page = await browser.newPage();
  page.setDefaultTimeout(30000);
  
  try {
    console.log('Navigating to Substack publish page...');
    await page.goto('https://engineeringforward.substack.com/publish/post', { waitUntil: 'networkidle2' });
    await new Promise(r => setTimeout(r, 5000));
    
    const currentUrl = await page.url();
    console.log('Current URL:', currentUrl);
    
    if (currentUrl.includes('sign-in')) {
      console.log('NOT_LOGGED_IN with Default/Default profile');
      await browser.close();
      process.exit(2);
    }
    
    let titleEl = await page.$('textarea.pencraft.page-title');
    if (!titleEl) {
      console.log('Title field not found, waiting...');
      await new Promise(r => setTimeout(r, 5000));
      titleEl = await page.$('textarea.pencraft.page-title');
    }
    
    if (!titleEl) {
      console.log('EDITOR_NOT_FOUND');
      await page.screenshot({ path: '/tmp/substack-editor.png' });
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
    
    await new Promise(r => setTimeout(r, 5000));
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
    await page.screenshot({ path: '/tmp/substack-published.png' });
    const finalUrl = await page.url();
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
  
  await browser.close();
})();