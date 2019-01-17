import requests
import urllib


import urllib.parse
s = urllib.parse.quote('Crossin 的编程教室')
print(s)
print(urllib.parse.unquote(s))

# name = '张艺谋'
# name = urllib.parse.quote(name)
# url = 'https://api.douban.com/v2/movie/new_movies'# + name
# print(url)
# req = urllib.request.urlopen(url)
# data = req.read()
# print(data)


# name = '张艺谋'
# name = urllib.parse.quote(name)
# url = 'https://api.douban.com/v2/movie/new_movies'# + name
# req = requests.get(url)
# print(req)
# print(req.status_code)
# data = req.json()


# proxies = {
#     'https': 'https://119.101.112.233:9999'
# }
# url = 'https://ddns.oray.com/checkip'
#
# req = requests.get(url, proxies=proxies)
# data = req.text
# print(data)

