// usage: node render.mjs jobs.json   jobs: [{html, out, w, h}]
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || '/opt/node-tools/node_modules/playwright');
import fs from 'fs';
const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
for (const j of jobs) {
  await page.setViewportSize({ width: j.w, height: j.h });
  await page.goto('file://' + j.html);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(150);
  await page.screenshot({ path: j.out, type: 'png' });
  console.log('rendered', j.out);
}
await browser.close();
