#!/usr/bin/env python
#coding = utf-8
#Author:CaoYang(157226691@qq.com)
#Time:2018/2/24 14:24

import requests
import re
from bs4 import BeautifulSoup

def cha(en):
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}
    url_head = r'http://dict.youdao.com/w/'
    url_end = r'/#keyfrom=dict2.top'
    url = url_head + en +url_end
    try:
        r = requests.get(url,headers=header)
        r.raise_for_status()
        #print(r.text)
    except:
        print('error')

    soup = BeautifulSoup(r.content,'lxml')
    aaa = soup.find_all('div',class_="trans-container")
    for i in aaa[0]:
        for j in i:
            print(BeautifulSoup(str(j)).string)

cha('little')
cha('hot')
