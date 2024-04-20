from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.cardratings.com/credit-card-list.html'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
soup_A = soup.find(id = 'div_A')

#file_path = 'C:\Users\ackim\Desktop\output.html'


cards_links = soup_A.find_all("span", {"class": "sh-active-client sh-quidget-rendered"}
                             #attrs={"data-rate-name": True, "data-content": True,}
)

#with open(file_path, 'w', encoding='utf-8') as file:
 #   file.write(str(cards_links))

#print(cards_links)

print(req.status_code)
#for i in range(25):
 #   letter = chr(ord('a')+i)
  #  s

unique_card = []

for cardlink in cards_links:
    name = cardlink['data-rate-name']
    if name not in unique_card:
        unique_card.append(name)
    ul = cardlink.find("ul")
    #print(cardlink)
    if ul:
        li = ul.find_all('li')
        for lis in li:
            print(li.text)
        #bullet_points = [li.text.strip() for li in ul.find_all('li')]
        #description = '\n'.join(bullet_points)  # Combines all bullet points into a single string
    else:
        description = "No description available"
    unique_card.append((name, description))
    #print(cardlink.get('href', 'error'))

for card in unique_card:
    print(card)