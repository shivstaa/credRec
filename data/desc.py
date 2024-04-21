from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import string

# Configure ChromeDriver options
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_argument('referer=https://www.google.com/')
options.add_argument('--headless')
options.add_argument('--enable-third-party-cookies')  # Attempt to allow third-party cookies
#options.add_argument("--log-level=3")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = 'https://www.cardratings.com/credit-card-list.html#div_D'
driver.get(url)
import asyncio
from pyppeteer import launch

async def run():
    browser = await launch(executablePath='path/to/your/chromium-or-chrome', headless=True)

async def run():
    # Launch the browser. Headless mode is default but can be set to False for debugging.
    browser = await launch(executablePath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", headless=True)
    page = await browser.newPage()

    # Go to the initial page
    await page.goto('https://www.cardratings.com/credit-card-list.html')

    # Wait for the page to load and for specific elements to be ready
    await page.waitForSelector('#div_A', options={'visible': True})
    
    # Interact with elements within #div_D or extract information
    content = await page.evaluate('''() => {
        const div = document.querySelector('#div_D');
        return div ? div.innerText : 'No content found';
    }''')
    
    print(content)

    # Optionally, interact with buttons or links within that div
    # Assuming there is a button with an id of 'loadMore' within div_D
    button_selector = '#div_D #loadMore'
    button = await page.querySelector(button_selector)
    if button:
        await button.click()
        await page.waitForNavigation()  # Wait for any potential navigation triggered by the button

    # Close the browser
    await browser.close()

# Run the asynchronous function
asyncio.run(run())