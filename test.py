
import requests
from bs4 import BeautifulSoup
url = "https://www.ukrinform.ru/"

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
   
r = requests.get(url=url, headers=headers)
    
soup = BeautifulSoup(r.text,"lxml")

lastNews = soup.find("div",class_='othersBody')
dllink = lastNews.find_next().find_next()("div",class_='othersDay').get('href')
print(dllink)