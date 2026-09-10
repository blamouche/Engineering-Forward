const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const file = path.join(__dirname, '20260909-post-what-the-review-becomes.md');
  const markdown = fs.readFileSync(file, 'utf8');

  // Extract title (first line starting with #)
  const title = markdown.match(/^# (.+)$/m)[1].trim();
  
  // Extract subtitle (line starting with * and ending with *)
  const subtitleMatch = markdown.match(/^\*(.+)\*$/m);
  const subtitle = subtitleMatch ? subtitleMatch[1].trim() : '';

  // Extract body: everything between subtitle and --- (Sources separator)
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
        // Convert links: [text](url) -> <a href="url">text</a>
        para = para.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
        // Convert bold
        para = para.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
        // Convert italic (but not in links)
        para = para.replace(/(?<!\*)\*([^*]+)\*(?!\*)/g, '<em>$1</em>');
        html += `<p>${para}</p>\n`;
        currentPara = [];
      }
    }
    
    for (let line of lines) {
      line = line.trimEnd();
      if (line === '') {
        if (inList) {
          html += '</ul>\n';
          inList = false;
        }
        flushPara();
        continue;
      }
      
      // Headings
      if (line.startsWith('## ')) {
        if (inList) { html += '</ul>\n'; inList = false; }
        flushPara();
        const heading = line.substring(3).replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
        html += `<h2>${heading}</h2>\n`;
        continue;
      }
      
      // List items
      if (line.startsWith('- ')) {
        flushPara();
        if (!inList) {
          html += '<ul>\n';
          inList = true;
        }
        let item = line.substring(2);
        item = item.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
        item = item.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
        html += `<li>${item}</li>\n`;
        continue;
      }
      
      // Numbered list items
      if (line.match(/^\d+\.\s/)) {
        flushPara();
        if (!inList) {
          html += '<ol>\n';
          inList = true;
        }
        let item = line.replace(/^\d+\.\s/, '');
        item = item.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
        html += `<li>${item}</li>\n>`;
        continue;
      }
      
      // Regular paragraph text
      if (inList) {
        html += '</ul>\n';
        inList = false;
      }
      currentPara.push(line.trim());
    }
    
    if (inList) {
      html += '</ul>\n';
    }
    flushPara();
    
    return html;
  }

  const bodyHtml = mdToHtml(body);
  
  console.log('Title:', title);
  console.log('Subtitle:', subtitle);
  console.log('Body HTML length:', bodyHtml.length);
  console.log('Body HTML preview:', bodyHtml.substring(0, 200));

  const browser = await chromium.launch({
    channel: 'chrome',
    headless: false,
  });
  
  const context = await browser.newContext({
    viewport: { width: 1280, height: 900 },
  });
  
  const page = await context.newPage();
  
  // Navigate to Substack publish page
  console.log('Navigating to Substack publish page...');
  await page.goto('https://engineeringforward.substack.com/publish/post', { waitUntil: 'networkidle', timeout: 30000 });
  
  // Wait for page to load
  await page.waitForTimeout(5000);
  
  // Check if we're logged in (look for the editor)
  const titleSelector = await page.$('textarea.pencraft.page-title');
  if (!titleSelector) {
    // Check if we need to log in
    const url = page.url();
    console.log('Current URL:', url);
    if (url.includes('login') || url.includes('sign-in') || url.includes('account')) {
      console.log('ERROR: Not logged in to Substack. Cannot publish.');
      await browser.close();
      process.exit(1);
    }
    // Maybe different selector
    console.log('Page title:', await page.title());
    console.log('Could not find title editor. Taking screenshot...');
    await page.screenshot({ path: path.join(__dirname, 'publish-debug.png') });
    console.log('Screenshot saved to substack/publish-debug.png');
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
  await page.evaluate((html) => {
    const editor = document.querySelector('.tiptap.ProseMirror');
    if (editor) {
      editor.focus();
      document.execCommand('selectAll', false, null);
      document.execCommand('insertHTML', false, html);
    }
  }, bodyHtml);
  
  await page.waitForTimeout(3000);
  
  // Wait for "Enregistré" / "Saved" status
  console.log('Waiting for save status...');
  await page.waitForTimeout(5000);
  
  // Click "Continuer" (Continue) button
  console.log('Looking for Continue button...');
  const continueButton = await page.$('button:has-text("Continuer")') || await page.$('button:has-text("Continue")');
  if (continueButton) {
    console.log('Clicking Continue...');
    await continueButton.click();
    await page.waitForTimeout(5000);
    
    // Wait for publishing screen
    console.log('Looking for publish button...');
    const publishButton = await page.$('button:has-text("Envoyer à tous maintenant")') || 
                          await page.$('button:has-text("Send to everyone now")') ||
                          await page.$('button:has-text("Publish now")');
    
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
      
      // Check for confirmation
      const currentUrl = page.url();
      console.log('Final URL:', currentUrl);
      
      if (currentUrl.includes('/publish/posts/detail/') || currentUrl.includes('/p/')) {
        console.log('SUCCESS: Post published!');
        console.log('Post URL: https://engineeringforward.substack.com/p/what-the-review-becomes');
      } else {
        console.log('Taking screenshot to check status...');
        await page.screenshot({ path: path.join(__dirname, 'publish-result.png') });
        console.log('Screenshot saved to substack/publish-result.png');
      }
    } else {
      console.log('Could not find publish button.');
      await page.screenshot({ path: path.join(__dirname, 'publish-no-button.png') });
    }
  } else {
    console.log('Could not find Continue button.');
    await page.screenshot({ path: path.join(__dirname, 'publish-no-continue.png') });
  }
  
  await browser.close();
  console.log('Done.');
})();