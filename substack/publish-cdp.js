const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const file = path.join(__dirname, '20260909-post-what-the-review-becomes.md');
  const markdown = fs.readFileSync(file, 'utf8');

  // Extract title
  const title = markdown.match(/^# (.+)$/m)[1].trim();
  
  // Extract subtitle
  const subtitleMatch = markdown.match(/^\*(.+)\*$/m);
  const subtitle = subtitleMatch ? subtitleMatch[1].trim() : '';

  // Extract body
  const bodyStart = markdown.indexOf('*', markdown.indexOf('\n') + 1);
  const bodyEnd = markdown.indexOf('\n---\n', bodyStart);
  let body = markdown.substring(bodyStart, bodyEnd).replace(/^\*.+\*\n+/, '').trim();

  // Convert markdown body to HTML
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
  console.log('Body HTML length:', bodyHtml.length);

  // Connect to running Chrome via CDP
  console.log('Connecting to running Chrome on port 9222...');
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  
  const contexts = browser.contexts();
  console.log('Found', contexts.length, 'browser contexts');
  
  const context = contexts[0];
  const pages = context.pages();
  console.log('Found', pages.length, 'open pages');
  
  // Create a new page
  const page = await context.newPage();
  
  // Navigate to Substack publish page
  console.log('Navigating to Substack publish page...');
  await page.goto('https://engineeringforward.substack.com/publish/post', { waitUntil: 'networkidle', timeout: 30000 });
  
  await page.waitForTimeout(5000);
  
  const currentUrl = page.url();
  console.log('Current URL:', currentUrl);
  
  // Check if we're logged in
  if (currentUrl.includes('sign-in') || currentUrl.includes('login')) {
    console.log('ERROR: Not logged in to Substack.');
    await page.screenshot({ path: path.join(__dirname, 'login-required.png') });
    await browser.close();
    process.exit(1);
  }
  
  // Look for the title editor
  console.log('Looking for editor...');
  const titleEl = await page.$('textarea.pencraft.page-title');
  
  if (!titleEl) {
    console.log('Could not find title editor. Trying alternative selectors...');
    // Try to find any textarea
    const textareas = await page.$$('textarea');
    console.log('Found', textareas.length, 'textareas on page');
    await page.screenshot({ path: path.join(__dirname, 'editor-debug.png') });
    console.log('Screenshot saved.');
    await browser.close();
    process.exit(1);
  }
  
  console.log('Found editor. Filling in title...');
  
  // Fill title
  await page.evaluate((t) => {
    const el = document.querySelector('textarea.pencraft.page-title');
    el.value = t;
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
  }, title);
  
  await page.waitForTimeout(1000);
  
  // Fill subtitle
  await page.evaluate((s) => {
    const el = document.querySelector('textarea.pencraft.subtitle');
    if (el) {
      el.value = s;
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }, subtitle);
  
  await page.waitForTimeout(1000);
  
  // Insert body into editor
  console.log('Inserting body content...');
  await page.evaluate((htmlContent) => {
    const editor = document.querySelector('.tiptap.ProseMirror');
    if (editor) {
      editor.focus();
      document.execCommand('selectAll', false, null);
      document.execCommand('insertHTML', false, htmlContent);
    }
  }, bodyHtml);
  
  await page.waitForTimeout(5000);
  
  // Wait for save status
  console.log('Waiting for save...');
  await page.waitForTimeout(3000);
  
  // Click "Continuer" (Continue) button
  console.log('Looking for Continue button...');
  const continueSelectors = [
    'button:has-text("Continuer")',
    'button:has-text("Continue")',
  ];
  
  let continueButton = null;
  for (const sel of continueSelectors) {
    continueButton = await page.$(sel);
    if (continueButton) break;
  }
  
  if (continueButton) {
    console.log('Clicking Continue...');
    await continueButton.click();
    await page.waitForTimeout(5000);
    
    // Wait for publishing screen
    console.log('Looking for publish button...');
    const publishSelectors = [
      'button:has-text("Envoyer à tous maintenant")',
      'button:has-text("Send to everyone now")',
      'button:has-text("Publish now")',
      'button:has-text("Publier")',
    ];
    
    let publishButton = null;
    for (const sel of publishSelectors) {
      publishButton = await page.$(sel);
      if (publishButton) break;
    }
    
    if (publishButton) {
      console.log('Clicking publish...');
      await publishButton.click();
      await page.waitForTimeout(3000);
      
      // Check for "Publier sans boutons" dialog
      const noButtonsBtn = await page.$('button:has-text("Publier sans boutons")') || 
                           await page.$('button:has-text("Publish without buttons")');
      if (noButtonsBtn) {
        console.log('Clicking publish without buttons...');
        await noButtonsBtn.click();
        await page.waitForTimeout(5000);
      }
      
      const finalUrl = page.url();
      console.log('Final URL:', finalUrl);
      
      // Check page content for "Publié" status
      const pageText = await page.evaluate(() => document.body.innerText);
      if (pageText.includes('Publié') || finalUrl.includes('/publish/posts/detail/')) {
        console.log('SUCCESS: Post published!');
        console.log('Post URL: https://engineeringforward.substack.com/p/what-the-review-becomes');
      } else {
        console.log('Status text snippet:', pageText.substring(0, 500));
        await page.screenshot({ path: path.join(__dirname, 'publish-result.png') });
      }
    } else {
      console.log('Could not find publish button.');
      const pageText = await page.evaluate(() => document.body.innerText);
      console.log('Page text snippet:', pageText.substring(0, 500));
      await page.screenshot({ path: path.join(__dirname, 'publish-no-button.png') });
    }
  } else {
    console.log('Could not find Continue button.');
    await page.screenshot({ path: path.join(__dirname, 'publish-no-continue.png') });
  }
  
  // Don't close the browser since it's the user's running instance
  // Just close our page
  // await page.close();
  // await browser.close();
  console.log('Done.');
})();