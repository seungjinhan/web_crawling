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
 
 
# 거래상위  (코스피)
url = 'https://finance.naver.com/sise/sise_quant.nhn?sosok=0'
req = requests.get(url)

## HTML 소스 가져오기
html = req.text
soup = BeautifulSoup(html, 'html.parser')
data = soup.find("table", class_='type_2')
list_data = data.find_all('tr')

index = 0
for tr in list_data:
    
    if index > 1 :
        
        #print( tr)
        td_list = tr.find_all('td')
        if( len( td_list) == 12):

            print('--------------------')
            no          = td_list[0] # 종목명
            name        = td_list[1] # 종목명
            now_price   = td_list[2] # 현재가
            compare_y   = td_list[3] # 전일비
            percent     = td_list[4] # 등락률
            all_count   = td_list[5] # 거래량
            money       = td_list[6] # 거래대금
            buy         = td_list[7] # 매수호가
            sell        = td_list[8] # 매도호가
            com_money   = td_list[9] # 시가총액
            per         = td_list[10] # PER
            roe         = td_list[11] # ROE
            
            print( no.contents[0])
            print( name.a['href'])
            print( name.a.contents[0])
            print( now_price.contents[0])
            
            if compare_y.img:
                print( compare_y.img['alt'])
                
            print( compare_y.span.contents[0])
            print( percent.span.contents[0])
            print( all_count.contents[0])
            print( money.contents[0])
            print( buy.contents[0])
            print( sell.contents[0])
            print( com_money.contents[0])
            print( per.contents[0])
            print( roe.contents[0])
          
            
    index = index +1;
    
# 거래상위  (코스닥)
url = 'https://finance.naver.com/sise/sise_quant.nhn?sosok=1'
req = requests.get(url)

## HTML 소스 가져오기
html = req.text
soup = BeautifulSoup(html, 'html.parser')
data = soup.find("table", class_='type_2')
list_data = data.find_all('tr')

index = 0
for tr in list_data:
    
    if index > 1 :
        
        #print( tr)
        td_list = tr.find_all('td')
        if( len( td_list) == 12):

            print('--------------------')
            no          = td_list[0] # 종목명
            name        = td_list[1] # 종목명
            now_price   = td_list[2] # 현재가
            compare_y   = td_list[3] # 전일비
            percent     = td_list[4] # 등락률
            all_count   = td_list[5] # 거래량
            money       = td_list[6] # 거래대금
            buy         = td_list[7] # 매수호가
            sell        = td_list[8] # 매도호가
            com_money   = td_list[9] # 시가총액
            per         = td_list[10] # PER
            roe         = td_list[11] # ROE
            
            print( no.contents[0])
            print( name.a['href'])
            print( name.a.contents[0])
            print( now_price.contents[0])
            
            if compare_y.img:
                print( compare_y.img['alt'])
                
            print( compare_y.span.contents[0])
            print( percent.span.contents[0])
            print( all_count.contents[0])
            print( money.contents[0])
            print( buy.contents[0])
            print( sell.contents[0])
            print( com_money.contents[0])
            print( per.contents[0])
            print( roe.contents[0])
          
            
    index = index +1;
    
 
# 시가총액 상위(코스피 )
url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0'
req = requests.get(url)

## HTML 소스 가져오기
html = req.text
soup = BeautifulSoup(html, 'html.parser')
data = soup.find("table", class_='type_2')
list_data = data.find_all('tr')

index = 0
for tr in list_data:
    
    if index > 1 :
        
        td_list = tr.find_all('td')
        if( len( td_list) == 13):
    
            print('--------------------')
            no          = td_list[0] # 번호
            name        = td_list[1] # 종목명
            now_price   = td_list[2] # 현재가
            compare_y   = td_list[3] # 전일비
            percent     = td_list[4] # 등락률
            show_price  = td_list[5] # 액면가
            all_money   = td_list[6] # 시가총액
            all_stock   = td_list[7] # 상장주식수
            foriener    = td_list[8] # 외국인비율
            all_count   = td_list[9] # 거래량
            per         = td_list[10] # PER
            roe         = td_list[11] # ROE
            
            print( no.contents[0])
            print( name.a['href'])
            print( name.a.contents[0])
            print( now_price.contents[0])
            
            if compare_y.img:
                print( compare_y.img['alt'])
                
            print( compare_y.span.contents[0].strip())
            print( percent.span.contents[0].strip())
            print( show_price.contents[0])
            print( all_money.contents[0])
            print( all_stock.contents[0])
            print( foriener.contents[0])
            print( all_count.contents[0])
            print( per.contents[0])
            print( roe.contents[0])
          
            
    index = index +1;
    
# 시가총액 상위(코스닥 )
url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1'
req = requests.get(url)

## HTML 소스 가져오기
html = req.text
soup = BeautifulSoup(html, 'html.parser')
data = soup.find("table", class_='type_2')
list_data = data.find_all('tr')

index = 0
for tr in list_data:
    
    if index > 1 :
        
        td_list = tr.find_all('td')
        if( len( td_list) == 13):
    
            print('--------------------')
            no          = td_list[0] # 번호
            name        = td_list[1] # 종목명
            now_price   = td_list[2] # 현재가
            compare_y   = td_list[3] # 전일비
            percent     = td_list[4] # 등락률
            show_price  = td_list[5] # 액면가
            all_money   = td_list[6] # 시가총액
            all_stock   = td_list[7] # 상장주식수
            foriener    = td_list[8] # 외국인비율
            all_count   = td_list[9] # 거래량
            per         = td_list[10] # PER
            roe         = td_list[11] # ROE
            
            print( no.contents[0])
            print( name.a['href'])
            print( name.a.contents[0])
            print( now_price.contents[0])
            
            if compare_y.img:
                print( compare_y.img['alt'])
                
            print( compare_y.span.contents[0].strip())
            print( percent.span.contents[0].strip())
            print( show_price.contents[0])
            print( all_money.contents[0])
            print( all_stock.contents[0])
            print( foriener.contents[0])
            print( all_count.contents[0])
            print( per.contents[0])
            print( roe.contents[0])
          
            
    index = index +1;
    
        