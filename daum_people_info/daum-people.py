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
collection = db['people']

while True:
    
    #sleep(5) 
    page = page + 1
    if page == 18115 :
        break;
        
    url = 'http://100.daum.net/book/651/list?sort=vcnt&index=&page='+str(page)
    
    print(url)
    
    req = requests.get(url)
    
    ## HTML 소스 가져오기
    html = req.text
    
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('ul', class_="list_register")
    
    people_list = data[0].find_all('li')
    
    for people in people_list:
    
        print( people)
        tr = people.find('a', class_='thumb_register');
        if tr == None:
            img = ''
        else:
            img = tr.img['src']
            
        name = people.find('a', class_='link_register').contents[0]
        link = "http://100.daum.net"+people.find('a', class_='link_register')['href']
        info = people.find('span', class_='desc_register').contents[0]
        tag = people.find_all('a', class_='link_tag')
        
        print('-----------------------------------------')
        print(link)
        print(img)
        print(name)
        print(info)
        print(tag)
        
        if len(tag) > 0:
            tag_json = '['
            for i in tag:
                tag_json += '"'+i.contents[0] +'",'
                
            tags = tag_json[:-1] + ']'
        else:
            tags = '[]'
        print('-----------------------------------------')
        n_data = {
            'name':name,
            'link':link,
            'img':img,
            'info':info,
            'tags':json.loads(tags)
        }                        
        
        print( n_data)
        collection.insert( n_data)
                        