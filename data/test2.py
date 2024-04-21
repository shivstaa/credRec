from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

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
link_element = driver.find_element(By.CLASS_NAME, "div_D")
link_element.click()

# Use WebDriverWait to ensure the page has loaded the necessary elements
WebDriverWait(driver, 20).until(
    #EC.visibility_of_element_located((By.ID, "div_D"))
    EC.presence_of_element_located((By.ID, "onetrust-consent-sdk"))  # Adjust the ID based on actual content you need
)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
soup_A = soup.find(id='cardList')

cards_links = soup_A.find_all("div", {"class": "filterDiv"})

def download_webp_image_to_list(image_url):
    # Send a GET request to the image URL
    response = requests.get(image_url)
    
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Return the content of the response (the image data)
        return response.content
    else:
        print("Failed to retrieve WebP image. Status code:", response.status_code)
        return None

unique_card = []

for cardlink in cards_links:
    element = cardlink.find("a", class_="sh-active-client sh-quidget-rendered")
    if element:
        name = element.get("title")
        if name:
            name = name.replace("Apply Now for ", "")
        link = element["href"]
        creditNeededSpan = cardlink.find("span", class_="credit_needed font-weight-semibold")
        creditNeeded = creditNeededSpan.text
        img_element = cardlink.find("img")
        imagesource = img_element["src"]
        #image_data = download_webp_image_to_list(imagesource)

    # description = "No description available"  # Default description
    ul = cardlink.find("ul")

    if not ul: 
        pass

    if ul:
        description = ul.text.strip()  # Extract text and strip any excess whitespace
    
    if name not in unique_card and name is not None:  # Prevent duplicate card names
        unique_card.append((name, link, description, creditNeeded, imagesource))  # Store as a tuple for better structure
        #print(type(image_data))
# Output the results
for card in unique_card:
    print(card)
