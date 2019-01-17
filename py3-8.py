# -*- coding:utf-8 -*-

import requests
import csv

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
show_offset = [1547690648000000]


def get_info(url):
    global show_offset
    req = requests.get(url, headers=headers)
    data = req.json()
    show_offset.append(data['shown_offset'])
    info = []
    for item in data['articles']:
        try:
            info.append([item['title'], item['user_name'], item['views']])
            # print('info:', info)
        except Exception as e:
            print('error:', e)
            continue
    return info


def savecsv(all_data):
    with open('csvpy3-8.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题', '用户', '点击数'])
        for data in all_data:
            writer.writerow(data)


def main():
    global show_offset
    url_origin = 'https://www.csdn.net/api/articles?type=more&category=newarticles&shown_offset={}'

    all_data = []
    for i in range(3):
        offset = show_offset.pop()
        url = url_origin.format(offset)
        print('url:', url)
        lst_info = get_info(url)
        # print('lst_info:', lst_info)
        all_data.extend(lst_info)
        # print('all_data:', all_data)
    savecsv(all_data)


if __name__ == '__main__':
    main()
