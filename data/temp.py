from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import TimeoutException


# Configure ChromeDriver options
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_argument('referer=https://www.google.com/')
options.add_argument('--headless')
options.add_argument('--enable-third-party-cookies')  # Attempt to allow third-party cookies
options.add_argument("--log-level=3")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = 'https://www.cardratings.com/credit-card-list.html#div_D'
driver.get(url)


# List to hold all unique cards from all divs
all_cards = []

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Loop over the IDs from div_A to div_Z
for char in range(ord('D'), ord('Z')+1):
    div_id = f"div_{chr(char)}"
    link_element = driver.find_element(By.CLASS_NAME, div_id)
    link_element.click()
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "onetrust-consent-sdk")))

        current_div = soup.find(id='cardList')
        if current_div:
            cards_links = current_div.find_all("div", {"class": "filterDiv"})
            for cardlink in cards_links:
                element = cardlink.find("a", class_="sh-active-client sh-quidget-rendered")
                if element:
                    name = element.get(0, 'data-rate-name')
                    link = element["href"]
                    creditNeededSpan = cardlink.find("span", class_="credit_needed font-weight-semibold")
                    creditNeeded = creditNeededSpan.text
                    img_element = cardlink.find("img")
                    imagesource = img_element["src"]
                    #image_data = download_webp_image_to_list(imagesource)
                ul = cardlink.find("ul")

                if not ul: 
                    pass

                if ul:
                    description = ul.text.strip()  # Extract text and strip any excess whitespace
    
                if name not in all_cards and description not in all_cards:  # Prevent duplicate card names
                    all_cards.append((name, link, description, creditNeeded, imagesource))  # Store as a tuple for better structure
                    #print(type(image_data))
    except TimeoutException:
        print(f"Timeout or element not found for {div_id}")

# Output the results
# for card in all_cards:
#     print(card)
with open('div_D-Z.txt', 'w') as f:
    for line in all_cards:
        f.write(f"{line}\n")