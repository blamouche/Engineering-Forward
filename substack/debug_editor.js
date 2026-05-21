const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
  console.log('Connecting to Chrome via CDP...');
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const contexts = browser.contexts();
  const pages = contexts[0]?.pages() || [];
  let page = pages.find(p => p.url().includes('substack')) || pages[0];
  
  console.log('Loading existing draft page...');
  await page.goto('https://engineeringforward.substack.com/publish/post/draft', {
    waitUntil: 'networkidle', timeout: 15000
  });
  await sleep(5000);
  
  // Read markdown and build JSON
  const mdContent = fs.readFileSync(path.join(__dirname, 'latest.md'), 'utf-8');
  const lines = mdContent.split('\n');
  
  let title = '';
  for (const line of lines) {
    if (line.startsWith('# ')) { title = line.replace(/^# /, '').trim(); break; }
  }

  // Debug: check what the bodyEl.editor looks like
  const debugInfo = await page.evaluate(() => {
    const bodyEl = document.querySelector('[data-placeholder="Start writing..."]');
    if (!bodyEl) return 'no-body-el';
    
    const editor = bodyEl.editor;
    if (!editor) return 'no-editor';
    
    // Get current content JSON schema
    const currentJSON = editor.getJSON();
    const schema = editor.schema;
    const nodes = schema.nodes ? Object.keys(schema.nodes) : [];
    const marks = schema.marks ? Object.keys(schema.marks) : [];
    
    return {
      currentJSON: JSON.stringify(currentJSON).slice(0, 500),
      nodeTypes: nodes,
      markTypes: marks,
      isEditable: editor.isEditable,
      storage: editor.storage ? Object.keys(editor.storage) : []
    };
  });
  
  console.log('Debug info:', debugInfo);
  
  // Now try to set content with a simpler test first
  const testResult = await page.evaluate(() => {
    const bodyEl = document.querySelector('[data-placeholder="Start writing..."]');
    if (!bodyEl?.editor) return 'no-editor';
    
    const editor = bodyEl.editor;
    
    // Try setting a simple test content
    const testJSON = {
      type: 'doc',
      content: [
        {
          type: 'paragraph',
          content: [{ type: 'text', text: 'TEST PARAGRAPH - if you see this, injection works' }]
        }
      ]
    };
    
    editor.commands.setContent(testJSON);
    return JSON.stringify(editor.getJSON()).slice(0, 300);
  });
  
  console.log('Test result:', testResult);
  
  await sleep(2000);
  await page.screenshot({ path: path.join(__dirname, 'debug_test_injection.png'), fullPage: true });
  
  console.log('Debug screenshot saved.');
}

main().catch(err => console.error('Error:', err));
