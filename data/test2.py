from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_argument('referer=https://www.google.com/')
options.add_argument('--headless')


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = 'https://www.cardratings.com/credit-card-list.html'
driver.get(url)
driver.implicitly_wait(10) 

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
soup_A = soup.find(id = 'div_A')

#file_path = 'C:\Users\ackim\Desktop\output.html'


cards_links = soup_A.find_all("span", {"class": "sh-active-client sh-quidget-rendered"}
                             #attrs={"data-rate-name": True, "data-content": True,}
)


unique_card = []

for cardlink in cards_links:
    name = cardlink['data-rate-name']
    if name not in unique_card:
        unique_card.append(name)
    ul = cardlink.find("ul")
    #print(cardlink)
    if ul:
        print(ul)
        # li = ul.find_all('li')
        # for lis in li:
        #     print(li.text)
        #bullet_points = [li.text.strip() for li in ul.find_all('li')]
        #description = '\n'.join(bullet_points)  # Combines all bullet points into a single string
    else:
        description = "No description available"
    unique_card.append((name, description))
    #print(cardlink.get('href', 'error'))

for card in unique_card:
    print(card)