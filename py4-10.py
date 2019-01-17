import requests
import pymongo

client = pymongo.MongoClient()
db = client.kugousongs
collections = db.songsss


def search(keyinput):
    page = 1
    pagesize = 50
    url_origin = 'http://songsearch.kugou.com/song_search_v2?keyword={}&page={}&pagesize={}'
    url = url_origin.format(keyinput, page, pagesize)

    while True:
        print('这次循环的', url)
        req = requests.get(url)
        data = req.json()
        collections.insert_many(data['data']['lists'])
        totalsongs = data['data']['total']
        print(totalsongs)
        if totalsongs <= (page*pagesize):
            break
        page += 1
        print(page)
        url = url_origin.format(keyinput, page, pagesize)
        print('下次循环的',url)
        print(page*pagesize)
        print('======================')


def get_lyric():
    url_detail = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash='
    for song in collections.find():
        songhash = song['FileHash']
        try:
            req = requests.get(url_detail+str(songhash))
            detail_data = req.json()
            print('updating', detail_data['data']['hash'])
            # print(collections)
            collections.update_one({'FileHash': songhash},{'$set':{'lyrics':detail_data['data']['lyrics']}},upsert =True)
            print('done', detail_data['data']['hash'])
        except Exception as e:
            print('error:', e)


keyinput = input('输入搜索关键字：\n')
search(keyinput)
get_lyric()



