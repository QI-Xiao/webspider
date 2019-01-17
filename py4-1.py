import requests
import pymongo

client = pymongo.MongoClient()
db = client.douban
collections = db.movies

for start in range(0, 100, 20):
    print('fetching', start)
    url = 'https://api.douban.com/v2/movie/top250?start=' + str(start)
    req = requests.get(url)
    data = req.json()
    print('insert', start)
    collections.insert_many(data['subjects'])
    print('done', start)
    # for movie in data['subjects']:
    #     print(movie['title'])