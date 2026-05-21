const { chromium } = require('playwright');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const pages = browser.contexts()[0].pages();
  let page = pages.find(p => p.url().includes('substack')) || pages[0];
  
  await page.goto('https://engineeringforward.substack.com/publish/post/draft', { waitUntil: 'networkidle', timeout: 15000 });
  await sleep(6000);
  
  // Dump the editor structure
  const info = await page.evaluate(() => {
    const result = { editables: [], inputs: [], textareas: [] };
    
    document.querySelectorAll('[contenteditable="true"]').forEach(el => {
      result.editables.push({
        tag: el.tagName,
        dataPh: el.getAttribute('data-placeholder'),
        ph: el.getAttribute('placeholder'),
        ariaLabel: el.getAttribute('aria-label'),
        role: el.getAttribute('role'),
        class: el.className?.slice(0, 80),
        text: el.textContent?.slice(0, 80),
        hasEditor: !!el.editor
      });
    });
    
    document.querySelectorAll('input[type="text"], input:not([type])').forEach(el => {
      if (el.offsetParent) { // visible
        result.inputs.push({
          name: el.name,
          ph: el.placeholder,
          class: el.className?.slice(0, 60),
          value: el.value?.slice(0, 80)
        });
      }
    });
    
    document.querySelectorAll('textarea').forEach(el => {
      if (el.offsetParent) {
        result.textareas.push({
          ph: el.placeholder,
          class: el.className?.slice(0, 60),
          value: el.value?.slice(0, 80)
        });
      }
    });
    
    return result;
  });
  
  console.log(JSON.stringify(info, null, 2));
})();
