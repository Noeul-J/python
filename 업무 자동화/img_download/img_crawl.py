from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request
import pandas as pd
from multiprocessing import Pool

# key=pd.read_csv('./keyword.txt',encoding='cp949',names=['keyword'])
# keyword=[]
# [keyword.append(key['keyword'][x]) for x in range(len(key))]


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error : Creating directory. ' + directory)


def img_download(url):
    create_folder('./img')

    chromedriver = 'C:\\Users\\eden220706\\AppData\\Local\\EDEN TNS\\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(3)

    #페이지 이동
    driver.get(url)

    driver.find_element_by_xpath('//*[@id="query"]').send_keys('구름')
    driver.find_element_by_xpath('//button[@class="btn_search"]').click()
    time.sleep(0.5)

    driver.find_element_by_xpath('//a[.="이미지"]').click()

    # elem.send_keys(Keys.PAGE_DOWN)
    # time.sleep(0.1)
    # a = driver.find_elements_by_css_selector('')
    # urllib.request.urlretrieve(url, '파일이름')

    # driver.close()


if __name__ == '__main__':
    url = 'https://www.naver.com/'
    img_download(url)
    # pool = Pool(processes=4)  # 4개의 프로세스를 사용합니다.
    # pool.map(img_download, keyword)
