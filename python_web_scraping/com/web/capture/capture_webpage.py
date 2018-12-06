'''
Created on 2018. 10. 21.

@author: seungjin.han
@author: hanblues@gmail.com
'''

from selenium import webdriver

if __name__ == '__main__':
    url='http://naver.com'
    
    bw = webdriver.PhantomJS(executable_path='E:/dev/python/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    bw.implicitly_wait(3)
    bw.get(url)
    bw.save_screenshot("test.png")
    bw.quit()