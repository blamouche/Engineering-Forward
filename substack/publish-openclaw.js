const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const file = path.join(__dirname, '20260909-post-what-the-review-becomes.md');
  const markdown = fs.readFileSync(file, 'utf8');
  const title = markdown.match(/^# (.+)$/m)[1].trim();
  const subtitleMatch = markdown.match(/^\*(.+)\*$/m);
  const subtitle = subtitleMatch ? subtitleMatch[1].trim() : '';
  const bodyStart = markdown.indexOf('*', markdown.indexOf('\n') + 1);
  const bodyEnd = markdown.indexOf('\n---\n', bodyStart);
  let body = markdown.substring(bodyStart, bodyEnd).replace(/^\*.+\*\n+/, '').trim();

  function mdToHtml(md) {
    let html = '';
    const lines = md.split('\n');
    let inList = false;
    let currentPara = [];
    function flushPara() {
      if (currentPara.length > 0) {
        let para = currentPara.join(' ');
        para = para.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
        para = para.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
        para = para.replace(/(?<!\*)\*([^*]+)\*(?!\*)/g, '<em>$1</em>');
        html += `<p>${para}</p>\n`;
        currentPara = [];
      }
    }
    for (let line of lines) {
      line = line.trimEnd();
      if (line === '') {
        if (inList) { html += '</ul>\n'; inList = false; }
        flushPara();
        continue;
      }
      if (line.startsWith('## ')) {
        if (inList) { html += '</ul>\n'; inList = false; }
        flushPara();
        const heading = line.substring(3).replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
        html += `<h2>${heading}</h2>\n`;
        continue;
      }
      if (line.startsWith('- ')) {
        flushPara();
        if (!inList) { html += '<ul>\n'; inList = true; }
        let item = line.substring(2);
        item = item.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
        item = item.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
        html += `<li>${item}</li>\n`;
        continue;
      }
      if (line.match(/^\d+\.\s/)) {
        flushPara();
        if (!inList) { html += '<ol>\n'; inList = true; }
        let item = line.replace(/^\d+\.\s/, '');
        item = item.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
        html += `<li>${item}</li>\n`;
        continue;
      }
      if (inList) { html += '</ul>\n'; inList = false; }
      currentPara.push(line.trim());
    }
    if (inList) html += '</ul>\n';
    flushPara();
    return html;
  }
  const bodyHtml = mdToHtml(body);
  console.log('Title:', title);
  console.log('Subtitle:', subtitle);

  // Use openclaw Chrome profile
  const profileDir = '/Users/openclaw/Library/Application Support/Google/Chrome/openclaw';
  console.log('Launching with openclaw profile...');
  
  const browser = await chromium.launchPersistentContext(profileDir, {
    channel: 'chrome',
    headless: false,
    viewport: { width: 1280, height: 900 },
    args: ['--no-first-run', '--disable-default-apps', '--profile-directory=Default'],
  });
  
  const page = await browser.newPage();
  console.log('Navigating to Substack publish page...');
  await page.goto('https://engineeringforward.substack.com/publish/post', { waitUntil: 'networkidle', timeout: 30000 });
  await page.waitForTimeout(5000);
  
  const currentUrl = page.url();
  console.log('Current URL:', currentUrl);
  
  if (currentUrl.includes('sign-in') || currentUrl.includes('login')) {
    console.log('ERROR: Not logged in with openclaw profile either.');
    await browser.close();
    process.exit(1);
  }
  
  console.log('Looking for editor...');
  const titleEl = await page.$('textarea.pencraft.page-title');
  if (!titleEl) {
    console.log('No editor found.');
    await page.screenshot({ path: path.join(__dirname, 'editor-debug-openclaw.png') });
    await browser.close();
    process.exit(1);
  }
  
  console.log('Filling title...');
  await page.evaluate((t) => {
    const el = document.querySelector('textarea.pencraft.page-title');
    el.value = t;
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
  }, title);
  await page.waitForTimeout(1000);
  
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
  await page.evaluate((htmlContent) => {
    const editor = document.querySelector('.tiptap.ProseMirror');
    if (editor) {
      editor.focus();
      document.execCommand('selectAll', false, null);
      document.execCommand('insertHTML', false, htmlContent);
    }
  }, bodyHtml);
  await page.waitForTimeout(5000);
  
  console.log('Looking for Continue button...');
  let continueButton = await page.$('button:has-text("Continuer")') || await page.$('button:has-text("Continue")');
  
  if (continueButton) {
    console.log('Clicking Continue...');
    await continueButton.click();
    await page.waitForTimeout(5000);
    
    console.log('Looking for publish button...');
    let publishButton = await page.$('button:has-text("Envoyer à tous maintenant")') || 
                        await page.$('button:has-text("Send to everyone now")') ||
                        await page.$('button:has-text("Publish now")');
    
    if (publishButton) {
      console.log('Clicking publish...');
      await publishButton.click();
      await page.waitForTimeout(3000);
      
      let noButtonsBtn = await page.$('button:has-text("Publier sans boutons")') || 
                        await page.$('button:has-text("Publish without buttons")');
      if (noButtonsBtn) {
        console.log('Clicking publish without buttons...');
        await noButtonsBtn.click();
        await page.waitForTimeout(5000);
      }
      
      const finalUrl = page.url();
      console.log('Final URL:', finalUrl);
      const pageText = await page.evaluate(() => document.body.innerText);
      if (pageText.includes('Publié') || finalUrl.includes('/publish/posts/detail/')) {
        console.log('SUCCESS: Post published!');
      } else {
        console.log('Page text snippet:', pageText.substring(0, 500));
        await page.screenshot({ path: path.join(__dirname, 'publish-result.png') });
      }
    } else {
      console.log('No publish button found.');
      await page.screenshot({ path: path.join(__dirname, 'publish-no-button.png') });
    }
  } else {
    console.log('No Continue button found.');
    await page.screenshot({ path: path.join(__dirname, 'publish-no-continue.png') });
  }
  
  await browser.close();
  console.log('Done.');
})();
