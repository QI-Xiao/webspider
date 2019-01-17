import requests
from bs4 import BeautifulSoup
import urllib.request
from threading import Thread


def down_pic(link):
    # print('downloading:', link)
    filename = link.split('/')[-1]
    retries = 0
    while retries < 3:
        try:
            pic = requests.get('http:' + link, timeout=10)
            with open('py2-5/' + filename, 'wb') as f:
                f.write(pic.content)
        except:
            retries += 1
            #print(filename, 'failed')
        else:
            #print(filename, 'saved')
            break


url = 'https://www.qiushibaike.com/imgrank/'
for i in range(1):
    print(url)
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, features="lxml")
    result = soup.find_all('div', class_="thumb")
    #print(result)

    for link in result:
        link = link.a.img.get('src')
        print(link)
        t = Thread(target=down_pic, args=(link,))
        t.start()

    current_page = soup.find_all('span', class_="current")
    next_page = int(current_page[0].text) + 1
    url = 'https://www.qiushibaike.com/imgrank/page/%d' % next_page
