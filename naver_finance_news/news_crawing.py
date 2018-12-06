import requests
from bs4 import BeautifulSoup
import datetime
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

while True:

    is_break = 0
    first_check = 0
    
    now = now + datetime.timedelta(days=day_index)
    nowDate = now.strftime('%Y%m%d');
        
    url = 'https://finance.naver.com/news/news_list.nhn?mode=RANK&date='+str(nowDate)+'&page='+str(index)+""
    print(url)
    req = requests.get(url)
    
    ## HTML 소스 가져오기
    html = req.text
    
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('ul', class_="simpleNewsList")
    
    print( len(data))
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
                
            for j in range(len(news)):
                
                if first_check == 0:
                
                    print("1.",first_title)
                    print("2.",news[j].a['title'])
                    if first_title == news[j].a['title']:
                        print('1')
                        first_title = ''
                        first_check = 0
                        is_break = 1
                        break;
                    else:
                        print('2')
                        first_title = news[j].a['title']
                        first_check = 1