'''
Created on 2018. 10. 21.

@author: seungjin.han
@author: hanblues@gmail.com
'''
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

if __name__ == '__main__':
    
    id = 'id'
    pw = 'pw'
    
    sess = requests.session()
    
    loing_info = { 
        'email':id,
        'password':pw,
        }
    url_login = '로그인 API'
    res = sess.post(url_login, data=loing_info)
    res.raise_for_status()
    
    url_my = '정보를 얻고 싶은 페이지 및 API'
    res = sess.post(url_my)
    res.raise_for_status()
    
    soup = BeautifulSoup(res.text, "html.parser")
    '''호출된 페이지 및 API결과 출력'''
    print( soup.prettify)