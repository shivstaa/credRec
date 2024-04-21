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
options.add_argument('--enable-third-party-cookies')  # Attempt to allow third-party cookies
options.add_argument("--log-level=3")
options.add_argument("--headless")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
unique_card = set()
for char in range(ord('D'), ord('Z')+1):
    result = ("div_" + chr(char))
    url=('https://www.cardratings.com/credit-card-list.html#' +result)
    driver.get(url)
    link_element = driver.find_element(By.CLASS_NAME, result)
    link_element.click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    soup_A = soup.find(id='cardList')
    cards_links = soup_A.find_all("div", {"class": "filterDiv"})
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
            if name:  # Prevent duplicate card names
                unique_card.add((name, link, description, creditNeeded, imagesource))  # Store as a tuple for better structure
            #print(type(image_data))
file_path = "output.txt"
with open(file_path, "w", encoding="utf-8") as file:
    # Iterate over each tuple in the list
    for item in unique_card:
        # Convert the tuple to a string and write it to the file
        file.write(f"{item}\n")

# Inform the user that the operation is complete
print(f"Data has been written to {file_path}")