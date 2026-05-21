const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function main() {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  
  // Get cookies from the authenticated session
  const contexts = browser.contexts();
  const cookies = await contexts[0].cookies();
  
  // Find Substack auth cookies
  const substackCookies = {};
  for (const c of cookies) {
    if (c.domain.includes('substack.com')) {
      substackCookies[c.name] = c.value;
    }
  }
  
  console.log('Substack cookies found:');
  for (const [name, value] of Object.entries(substackCookies)) {
    console.log(`  ${name}=${value.slice(0, 20)}...`);
  }
  
  // Save as .env format
  const envContent = `SUBSTACK_SID=${substackCookies['substack.sid'] || ''}
SID=${substackCookies['sid'] || ''}
SUBSTACK_LLI=${substackCookies['substack.lli'] || ''}
`;
  
  fs.writeFileSync(path.join(__dirname, 'substack_cookies.env'), envContent);
  console.log('Cookies saved to substack_cookies.env');
  
  // Also save as JSON for Python
  fs.writeFileSync(path.join(__dirname, 'substack_cookies.json'), JSON.stringify(substackCookies, null, 2));
  console.log('Cookies saved to substack_cookies.json');
}

main().catch(console.error);
