const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const articlePath = path.join(__dirname, 'substack', '20260928-post-the-dissolving-boundary.md');
  const md = fs.readFileSync(articlePath, 'utf8');

  const lines = md.split('\n');
  const title = lines[0].replace(/^# /, '');
  let subtitle = '';
  for (let i = 1; i < lines.length; i++) {
    const l = lines[i].trim();
    if (l.startsWith('*') && l.endsWith('*')) {
      subtitle = l.slice(1, -1);
      break;
    }
  }

  let bodyLines = [];
  let inBody = false;
  for (let i = 1; i < lines.length; i++) {
    const l = lines[i];
    if (l.trim().startsWith('*') && l.trim().endsWith('*') && !inBody) {
      inBody = true;
      continue;
    }
    if (inBody) {
      if (/^---\s*$/.test(l.trim())) break;
      bodyLines.push(l);
    }
  }
  const body = bodyLines.join('\n').trim();

  function mdToHtml(md) {
    let html = '';
    const lines = md.split('\n');
    let inList = false;
    let paraLines = [];
    function flushPara() {
      if (paraLines.length > 0) {
        html += `<p>${inlineMd(paraLines.join(' '))}</p>\n`;
        paraLines = [];
      }
    }
    function closeList() { if (inList) { html += `</ul>\n`; inList = false; } }
    for (const line of lines) {
      if (line.trim() === '') { flushPara(); closeList(); continue; }
      const h2 = line.match(/^##\s+(.*)/);
      if (h2) { flushPara(); closeList(); html += `<h2>${inlineMd(h2[1])}</h2>\n`; continue; }
      const li = line.match(/^-\s+(.*)/);
      if (li) { flushPara(); if (!inList) { html += `<ul>\n`; inList = true; } html += `<li>${inlineMd(li[1])}</li>\n`; continue; }
      closeList(); paraLines.push(line);
    }
    flushPara(); closeList();
    return html;
  }
  function inlineMd(text) {
    text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
    text = text.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    text = text.replace(/(?<!\*)\*(?!\*)([^*]+)\*(?!\*)/g, '<em>$1</em>');
    return text;
  }

  const bodyHtml = mdToHtml(body);
  console.log('Title:', title);
  console.log('Subtitle:', subtitle);
  console.log('Body HTML length:', bodyHtml.length);

  // Load stored auth cookies
  const authPath = path.join(require('os').homedir(), '.substack-auth.json');
  const storedCookies = JSON.parse(fs.readFileSync(authPath, 'utf8'));
  console.log(`Loaded ${storedCookies.length} auth cookies from ~/.substack-auth.json`);

  // Convert to Playwright cookie format
  const playwrightCookies = storedCookies.map(c => ({
    name: c.name,
    value: c.value,
    domain: c.domain,
    path: c.path || '/',
    expires: c.expires > 0 ? c.expires : -1,
    secure: c.secure,
    httpOnly: c.httpOnly,
    sameSite: c.sameSite === 'None' ? 'None' : c.sameSite === 'Lax' ? 'Lax' : 'Strict'
  }));

  // Launch browser with fresh profile + injected cookies
  console.log('Launching browser...');
  const browser = await chromium.launch({
    headless: false,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    args: ['--disable-blink-features=AutomationControlled', '--no-first-run', '--no-default-browser-check', '--disable-gpu']
  });

  const context = await browser.newContext({
    viewport: { width: 1280, height: 900 },
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
  });

  // Add cookies
  await context.addCookies(playwrightCookies);
  console.log('Cookies injected.');

  const page = await context.newPage();

  try {
    // Navigate to Substack home to verify login
    console.log('Navigating to Substack home...');
    await page.goto('https://engineeringforward.substack.com/', { waitUntil: 'networkidle', timeout: 60000 });
    await page.waitForTimeout(3000);
    console.log('Home URL:', page.url());

    // Navigate to publish page
    console.log('Navigating to Substack publish page...');
    await page.goto('https://engineeringforward.substack.com/publish/post', { waitUntil: 'networkidle', timeout: 60000 });
    await page.waitForTimeout(3000);

    const currentUrl = page.url();
    console.log('Current URL:', currentUrl);

    if (currentUrl.includes('/sign-in') || currentUrl.includes('/login')) {
      console.log('ERROR: Not logged in with stored cookies.');
      await page.screenshot({ path: '/tmp/substack-login.png' });
      await browser.close();
      process.exit(1);
    }

    // Wait for editor
    const titleSelector = 'textarea.pencraft.page-title';
    console.log('Waiting for editor...');
    await page.waitForSelector(titleSelector, { timeout: 30000 });
    console.log('Editor found!');

    // Fill title
    console.log('Filling title...');
    await page.fill(titleSelector, title);
    await page.waitForTimeout(500);

    // Fill subtitle
    const subtitleSelector = 'textarea.pencraft.subtitle';
    const subtitleEl = await page.$(subtitleSelector);
    if (subtitleEl) {
      console.log('Filling subtitle...');
      await page.fill(subtitleSelector, subtitle);
      await page.waitForTimeout(500);
    } else {
      console.log('No subtitle field found.');
    }

    // Fill body
    console.log('Filling body...');
    const editorSelector = '.tiptap.ProseMirror';
    await page.waitForSelector(editorSelector, { timeout: 10000 });
    await page.click(editorSelector);
    await page.waitForTimeout(300);
    await page.evaluate((html) => {
      document.execCommand('selectAll', false, null);
      document.execCommand('insertHTML', false, html);
    }, bodyHtml);
    await page.waitForTimeout(2000);

    // Wait for save
    console.log('Waiting for save...');
    await page.waitForTimeout(5000);

    // Click Continue
    console.log('Looking for Continue button...');
    const continueBtn = await page.$('button:has-text("Continuer"), button:has-text("Continue")');
    if (continueBtn) {
      console.log('Clicking Continue...');
      await continueBtn.click();
      await page.waitForTimeout(5000);
    } else {
      const buttons = await page.$$eval('button', btns => btns.map(b => b.textContent.trim())).catch(() => []);
      console.log('No Continue button. Available:', buttons);
    }

    // Publishing screen
    console.log('Waiting for publishing screen...');
    await page.waitForTimeout(3000);

    // Click publish/send
    console.log('Looking for Send/Publish button...');
    const sendBtn = await page.$('button:has-text("Envoyer"), button:has-text("Send"), button:has-text("Publish"), button:has-text("Publier")');
    if (sendBtn) {
      console.log('Clicking publish button...');
      await sendBtn.click();
      await page.waitForTimeout(3000);
    } else {
      const buttons2 = await page.$$eval('button', btns => btns.map(b => b.textContent.trim())).catch(() => []);
      console.log('No send button. Available:', buttons2);
    }

    // Handle subscription button dialog
    console.log('Checking for subscription dialog...');
    const noButtonsBtn = await page.$('button:has-text("sans boutons"), button:has-text("without buttons"), button:has-text("Publish without")');
    if (noButtonsBtn) {
      console.log('Clicking publish without buttons...');
      await noButtonsBtn.click();
      await page.waitForTimeout(5000);
    }

    // Wait for confirmation
    console.log('Waiting for confirmation...');
    await page.waitForTimeout(5000);
    const finalUrl = page.url();
    console.log('Final URL:', finalUrl);

    if (finalUrl.includes('/publish/posts/detail') || finalUrl.includes('/p/')) {
      console.log('SUCCESS: Post published!');
    } else {
      const pageText = await page.textContent('body').catch(() => '');
      if (pageText.includes('Publié') || pageText.includes('Published')) {
        console.log('SUCCESS: Post published (via page text)!');
      } else {
        console.log('Publish status unclear. URL:', finalUrl);
        await page.screenshot({ path: '/tmp/substack-final.png' });
      }
    }

    // Save updated cookies
    const newCookies = await context.cookies();
    const cookieData = newCookies.filter(c => c.domain.includes('substack')).map(c => ({
      name: c.name,
      value: c.value,
      domain: c.domain,
      path: c.path,
      expires: c.expires,
      httpOnly: c.httpOnly,
      secure: c.secure,
      sameSite: c.sameSite
    }));
    fs.writeFileSync(authPath, JSON.stringify(cookieData, null, 2));
    console.log(`Saved ${cookieData.length} updated cookies to ~/.substack-auth.json`);

    // Verify post is live
    console.log('Verifying post is live...');
    try {
      await page.goto('https://engineeringforward.substack.com/p/the-dissolving-boundary', { waitUntil: 'networkidle', timeout: 30000 });
      await page.waitForTimeout(3000);
      console.log('Live URL:', page.url());
      const titleEl = await page.$('h1');
      if (titleEl) {
        const liveTitle = await titleEl.textContent();
        console.log('Live title:', liveTitle);
      }
    } catch (e) {
      console.log('Could not verify live URL:', e.message);
    }

  } catch (error) {
    console.error('ERROR:', error.message);
    await page.screenshot({ path: '/tmp/substack-error.png' }).catch(() => {});
  } finally {
    await browser.close();
  }
})();