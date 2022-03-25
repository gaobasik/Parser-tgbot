import time
from operator import ge
from re import T
import requests
from bs4 import BeautifulSoup
import json


def get_allDay_news():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    url = "https://www.ukrinform.ru/"
    r = requests.get(url=url, headers=headers)
    
    soup = BeautifulSoup(r.text,"lxml")
    lastNews = soup.find("div",class_='othersBody').text.strip()
    
    fNews = lastNews.replace('  ','')
    print (fNews)
def get_first_news():
    # with open("news_dict.json") as file:
    #     news_dict = json.load(file)
    news_dict = {}
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    url = "https://www.ukrinform.ru/"
    r = requests.get(url=url, headers=headers)
    
    soup = BeautifulSoup(r.text,"lxml")

    allnews = soup.find("div",class_="othersBody") # собираем инфу и заносим в джейсон
    time = allnews.find("div",class_='othersDay')
    lastNews = time.find_next().find_next().find_next().text.strip()
    ybrProbel = lastNews.replace('  ','')
    news_dict[ybrProbel] = {
        "News": ybrProbel
    }
    with open("news_dict.json","w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)


def check_news_update():
    with open("news_dict.json") as file:
        news_dict  = json.load(file)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    url = "https://www.ukrinform.ru/"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text,"lxml")
    allnews = soup.find("div",class_="othersBody")
    fresh_news = {}

    time = allnews.find("div",class_='othersDay')
    lastNews = time.find_next().find_next().find_next().text.strip()
    ybrProbel = lastNews.replace('  ','')
    for news in allnews:
        time = allnews.find("div",class_='othersDay')
        lastNews = time.find_next().find_next().find_next().text.strip()
        ybrProbel = lastNews.replace('  ','')
        if ybrProbel in news_dict:
            print("уже есть")
            continue
        else:
            allnews = soup.find("div",class_="othersBody") # собираем инфу и заносим в джейсон
            time = allnews.find("div",class_='othersDay')
            lastNews = time.find_next().find_next().find_next().text.strip()
            ybrProbel = lastNews.replace('  ','')
            
                

            news_dict[ybrProbel] = {
                    "News": ybrProbel,
                    
            }
            print('добавлено')

            fresh_news[ybrProbel] = {
                "News": ybrProbel,
                
            }
    with open("news_dict.json","w") as file:
        json.dump(news_dict,file,indent=4, ensure_ascii=False)
    return fresh_news


         
    
    
   


def main():
        print(check_news_update())


if __name__ == "__main__":
    main()