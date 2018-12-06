import requests
from bs4 import BeautifulSoup
import datetime
from pymongo import MongoClient
from time import sleep
'''

url="https://finance.naver.com/news/news_list.nhn";
req = requests.get(url)

## HTML 소스 가져오기
html = req.text

soup = BeautifulSoup(html, 'html.parser')

data = soup.find("ul", class_="realtimeNewsList")

data_list = data.find_all("dl")

is_thumb = 0;
is_title = 0;
is_sum = 0;

for d in data_list:
    news = d.find_all(['dt','dd'])
    for d2 in news:
        
        type = d2['class'][0];
        
        if type == 'thumb':
            is_thumb = 1;
            print( d2.a.contents[0])
        elif type == 'articleSubject':
            is_title = 1;
            print( d2.a.contents[0])
            print("https://finance.naver.com/", d2.a['href'])
        elif type == 'articleSummary':
            is_sum = 1;
            print( d2.contents[0])
            
            
           ''' 
           
index = 1;
now = datetime.datetime.now()
day_index = 0;

first_title = ''
first_check = 0

client = MongoClient('localhost', 27017)
db = client['news']
collection = db['naver_finance_news	']

while True:

    is_break = 0
    first_check = 0
    
    now = now + datetime.timedelta(days=day_index)
    nowDate = now.strftime('%Y%m%d');

    sleep(1)   # 1초간 딜레이 시킴
         
    url = 'https://finance.naver.com/news/news_list.nhn?mode=RANK&date='+str(nowDate)+'&page='+str(index)+""
    print(url)
    req = requests.get(url)
    
    ## HTML 소스 가져오기
    html = req.text
    
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('ul', class_="simpleNewsList")
    
    if len(data) == 1 :
        
        day_index = -1
        index = 1
    else :
        day_index = 0
        index = index+1
        
        for i in range(len(data)):
        
            news = data[i].find_all('li')
            
            if is_break == 1:
                day_index = -1
                index = 1
                break;

            is_input = False;    
            for j in range(len(news)):
                
                if first_check == 0:
                
                    if first_title == news[j].a['title']:
                        first_title = ''
                        first_check = 0
                        is_break = 1
                        is_input = False
                        break;
                    else:
                        first_title = news[j].a['title']
                        first_check = 1
                        is_input = True
                else:
                    is_input = True

                #DB 에 저장한다.
                if is_input == True:
                    link = news[j].a
                    str_link = str(link).replace('<a href="' , '<a href="https://finance.naver.com')
                    str_link = str_link.replace('&amp;' , '&')
                    
                    title = news[j].a['title']
                    press = news[j].find_all('span' , class_='press')[0].contents[0] 
                    wdate = news[j].find_all('span' , class_='wdate')[0].contents[0]

                    findDataCount = collection.count_documents({'title':title})
                    if findDataCount == 0:
                        in_data = {
                            'title':title,
                            'link':str_link,
                            'press':press,
                            'wdate':wdate
                        }                        
                        collection.insert( in_data)
                        print( title)
                        
                    
                    