const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const delay = require('delay-random');

const uploadText = fs.readFileSync('upload_text.txt', 'utf8');
const videoPath = path.join(__dirname, 'final_video.mp4');

(async () => {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    
    await page.goto('https://www.youtube.com/upload');

    // Assume user logs in manually
    
    await delay({ min: 3000, max: 5000 });

    const [fileChooser] = await Promise.all([
        page.waitForFileChooser(),
        page.click('input[type=file]')
    ]);

    await fileChooser.accept([videoPath]);
    
    await page.type('input#title', 'Your Video Title');
    await page.type('textarea#description', 'Your video description');
    
    await page.click('#done-button');
    await delay({ min: 3000, max: 5000 });

    await browser.close();
})();
