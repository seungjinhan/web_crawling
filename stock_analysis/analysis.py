# -*- coding: utf-8 -*-
"""
crawling people info from daum
and save date in MongoDB

"""

import requests
from bs4 import BeautifulSoup
import datetime
from pymongo import MongoClient
from time import sleep
import json

page = 0;

client = MongoClient('localhost', 27017)
db = client['people_db']
collection = db['youtube']
   

#업종상위    
url = 'https://finance.naver.com/sise/sise_group.nhn?type=upjong'
req = requests.get(url)

## HTML 소스 가져오기
html = req.text
soup = BeautifulSoup(html, 'html.parser')
data = soup.find("table", class_='type_1')
list_data = data.find_all('tr')

index = 0
for tr in list_data:
    
    if index > 2 :
        
        #print( tr)
        td_list = tr.find_all('td')
        if( len( td_list) == 7):
           
            print('--------------------')
            name        = td_list[0] #업종별 시세명
            up          = td_list[1] # 전일대비
            all_count   = td_list[2] # 전체
            up_count    = td_list[3] # 상승
            same_count  = td_list[4] # 보합
            down_count  = td_list[5] # 하락
            up_graph    = td_list[6] # 등락 그래프 
            
            print( name.a.contents[0])
            print( 'https://finance.naver.com'+name.a['href'])
            print( up.span.contents[0].strip())
            print( all_count.contents[0])
            print( up_count.contents[0])
            print( same_count.contents[0])
            print( down_count.contents[0])
            print( up_graph.span.contents[0])
            
    index = index +1;



#업종상위    
url = 'https://finance.naver.com/sise/theme.nhn'
req = requests.get(url)

## HTML 소스 가져오기
html = req.text
soup = BeautifulSoup(html, 'html.parser')
data = soup.find("table", class_='type_1')
list_data = data.find_all('tr')

index = 0
for tr in list_data:
    
    if index > 2 :
        
        #print( tr)
        td_list = tr.find_all('td')
        if( len( td_list) == 8):
           
            print('--------------------')
            name        = td_list[0] #업종별 시세명
            up          = td_list[1] # 전일대비
            up_3day     = td_list[2] # 최근3일 등락률(평균)
            up_count    = td_list[3] # 상승
            same_count  = td_list[4] # 보합
            down_count  = td_list[5] # 하락
            main1    = td_list[6] # 주도주
            main2    = td_list[7] # 주도주
            
            print( name.a.contents[0])
            print( 'https://finance.naver.com'+name.a['href'])
            print( up.span.contents[0].strip())
            print( up_3day.span.contents[0].strip())
            print( up_count.contents[0])
            print( same_count.contents[0])
            print( down_count.contents[0])
            print( main1.img['alt'])
            print( 'https://finance.naver.com/'+main1.a['href'])
            print( main1.a.contents[0])
            print( main2.img['alt'])
            print( 'https://finance.naver.com/'+main2.a['href'])
            print( main2.a.contents[0])
            
    index = index +1;
    
    