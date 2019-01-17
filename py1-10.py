# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

pages = input('请输入页数\n')
url = 'https://www.qiushibaike.com/text/'
data_all = ''
for page in range(2, int(pages)+2):
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'lxml')
    results = soup.find('div', id='content-left').find_all('div', class_=re.compile('^article block untagged'))
    pagenow = soup.find('div', class_='content-block clearfix').find('span', class_='current').string
    for div in results:
        print('page:',page-1)
        print('page really:', pagenow)
        print(div.div.h2.string.strip())
        print(div.find('div',class_='content').span.get_text('\n', '<br />'))
        print(div.find('span',class_='stats-vote').i.string)
        print(div.find('span', class_='stats-comments').a.i.string)
        data_all += div.div.h2.string.strip() + '\t'
        data_all += div.find('span',class_='stats-vote').i.string + '\t'
        data_all += div.find('span', class_='stats-comments').a.i.string + '\n'# 作者
        data_all += div.find('div',class_='content').span.get_text('\n', '<br />') + '\n\n'

        # data_all += div.span.get_text('\n', '<br />')
        print('-------------')
    print('=================')

    url = 'https://www.qiushibaike.com/text/page/' + str(page)
    print(url)

with open('txtpy1-10.txt', 'w', encoding='utf-8') as f:
    f.write(data_all)
