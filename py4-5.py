import requests
import pymongo
import time
import threading

client = pymongo.MongoClient()
db = client.douban
collections = db.movies
col_casts = db.casts

proxies = {
    'https': 'https://119.101.112.233:9999'
}


def get_cast(id):
    if not id:
        return
    try:
        url = 'https://api.douban.com/v2/movie/celebrity/' + str(id)
        req = requests.get(url, proxies=proxies)
        print(req)
        data = req.json()
        print('updating', id)
        col_casts.update_one({'id': data['id']}, {'$set':data}, upsert=True)
        print('done', id)
    except Exception as e:
        print(e, id)


for movie in collections.find():
    casts = movie['casts']
    for cast in casts:
        print(cast['name'], cast['id'])
        # threading.Thread(target=get_cast, args=(cast['id'],)).start()
        get_cast(cast['id'])
        time.sleep(1.5)
