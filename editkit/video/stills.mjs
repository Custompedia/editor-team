// Render single frames WITHOUT rendering the video: the fast design loop.
// Usage: cd video && node stills.mjs 120 480 900 ...   -> video/out/f00120.jpg ...
import {bundle} from '@remotion/bundler';
import {renderStill, selectComposition, openBrowser} from '@remotion/renderer';
import path from 'path';
import fs from 'fs';
const frames = process.argv.slice(2).map(Number);
fs.mkdirSync('out', {recursive: true});
const serveUrl = await bundle({entryPoint: path.resolve('src/index.ts'), publicDir: path.resolve('public')});
const composition = await selectComposition({serveUrl, id: 'Edit'});
const browser = await openBrowser('chrome');
for (const f of frames) {
  await renderStill({composition, serveUrl, frame: f, output: `out/f${String(f).padStart(5, '0')}.jpg`, imageFormat: 'jpeg', jpegQuality: 80, puppeteerInstance: browser, scale: 0.5});
}
await browser.close({silent: true});
console.log('rendered', frames.length, 'stills');
