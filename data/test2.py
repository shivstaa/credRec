from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Configure ChromeDriver options
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_argument('referer=https://www.google.com/')
options.add_argument('--headless')
options.add_argument('--enable-third-party-cookies')  # Attempt to allow third-party cookies
options.add_argument("--log-level=3")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = 'https://www.cardratings.com/credit-card-list.html'
driver.get(url)

# Use WebDriverWait to ensure the page has loaded the necessary elements
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "div_A"))  # Adjust the ID based on actual content you need
)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
soup_A = soup.find(id='div_A')

cards_links = soup_A.find_all("div", {"class": True, "id": True})

unique_card = []

for cardlink in cards_links:
    print(cardlink)
    span = cardlink.find_all("span", {"class": "sh-active-client sh-quidget-rendered"})
    print("FUCKING LOOK RIGHT HEREEEEEEEEEEEE")
    print (span)
    name = span.get('data-rate-name', 'No Name Available')

    # description = "No description available"  # Default description
    ul = cardlink.find("ul")

    if not ul: 
        pass

    if ul:
        description = ul.text.strip()  # Extract text and strip any excess whitespace
    
    if name not in unique_card:  # Prevent duplicate card names
        unique_card.append((name, description))  # Store as a tuple for better structure

# Output the results
for card in unique_card:
    print(card)
