from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException

# Configure ChromeDriver options
options = Options()
options.add_argument('--headless')
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")


# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = 'https://www.cardratings.com/credit-card-list.html'
driver.get(url)

# List to hold all unique cards from all divs
all_cards = []

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Loop over the IDs from div_A to div_Z
for char in range(ord('A'), ord('Z')+1):
    div_id = f"div_{chr(char)}"
    print(chr(char))
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, div_id)))

        current_div = soup.find(id=div_id)
        if current_div:
            cards_links = current_div.find_all("span", {"class": "sh-active-client sh-quidget-rendered"})
            for cardlink in cards_links:
                name = cardlink.get('data-rate-name', 'No Name Available')
                ul = cardlink.find("ul")
                description = ul.text.strip() if ul else "No description available"
                card_info = (div_id, name, description)
                if (name, description) not in all_cards:
                    all_cards.append(card_info)
                    print(name, description)
    except TimeoutException:
        print(f"Timeout or element not found for {div_id}")

# Output the results
for card in all_cards:
    print(card)