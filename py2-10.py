# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from threading import Thread


def down_pic(link):
    filename = link.split('/')[-1]
    retries = 0
    while retries < 3:
        try:
            pic = requests.get(link, headers=headers)
            print(pic)
            with open('txtpy2-10/' + filename, 'wb') as f:
                f.write(pic.content)
        except:
            retries += 1
        else:
            print('done')
            break

url = 'https://pixabay.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'lxml')
results = soup.find_all("img", attrs={"srcset":True})

for link in results:
    link = link.get('src')
    print(link)
    t = Thread(target=down_pic, args=(link,))
    t.start()
