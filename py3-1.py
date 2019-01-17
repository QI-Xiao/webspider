import requests

url_1 = 'https://www.zhihu.com/api/v4/members/'
url_2 = '/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'

headers = {
    'Cookie': '_zap=5ff3c9db-ffc1-46d0-8c16-7861f709e14d; d_c0="AMCiMxsTxg6PThr_qdpLY3_IwX87NqBZ3GM=|1546590732"; q_c1=42867ef59b39474a9dc9ae4021fb5a62|1546590734000|1546590734000; __gads=ID=947fcd3fa49c0a80:T=1546853738:S=ALNI_MbBo77FcH1RFoyLLiVWxFK0EKtvQg; _xsrf=DD2eYrqa8VYOG0kavYd18l8Xe4dGVsS9; l_cap_id="ODViY2ZiOWJlZWRlNDIwYjk5YjIxY2NhZGI4OTM4YTM=|1546951456|9435a3a99e673978cb10e0f449f9c072c600fb85"; r_cap_id="ZDZkZDZjM2UzMGZjNDc2N2IwZDQyYmZkMzFlMjQyY2Q=|1546951456|309d45cdf64295f0208f8e6478d41a6851164e23"; cap_id="YWRmMGY1NjY3NGZjNDJjZTljZDkzZjEwZWE2YTAxMmM=|1546951456|3664f576565156339928c93b73a7c46fc10f7fd9"; tst=f; tgw_l7_route=1b9b7363f02f3a5519d03bdf813bc914; capsion_ticket="2|1:0|10:1547537832|14:capsion_ticket|44:NWU4M2VmNTViYzhjNGQ2MzkzMjBiOTgzZmZmMDI2YWU=|736c2af767ebd09fbd0a655e61e33d16cdaaa6e0549611fa9e48ae20fa85d862"; z_c0="2|1:0|10:1547537932|4:z_c0|92:Mi4xSWFIMERRQUFBQUFBd0tJekd4UEdEaVlBQUFCZ0FsVk5ETndxWFFCd1Rid1lMbzRWRjdNVjJqOGJLdnVwcWxXbzRR|ac08195a0c962294726a62e8fc34f3beb556c72cf7501955ac2c3a7345cbd5a6"; __utma=51854390.2003027445.1547123274.1547123274.1547538014.2; __utmb=51854390.0.10.1547538014; __utmc=51854390; __utmz=51854390.1547538014.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/follow; __utmv=51854390.100--|2=registration_date=20190115=1^3=entry_date=20190104=1',
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/people/crossin/following',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def get_following(user):
    global to_crawl, crawled
    print('crawling', user)
    url = url_1 + user + url_2
    for i in range(10):
    # while True:
        req = requests.get(url, headers=headers)
        data = req.json()

        for user in data['data']:
            if user['follower_count'] > 600000:
                token = user['url_token']
                if token not in to_crawl and token not in crawled:
                    print(user['name'])
                    to_crawl.append(token)

        paging = data['paging']
        if paging['is_end']:
            break
        url = paging['next'].replace('/members', '/api/v4/members')
    print('to crawl', to_crawl)
    print('crawled', crawled)


to_crawl = ['crossin']
crawled = []

while len(to_crawl) > 0:
    user = to_crawl.pop()
    crawled.append(user)
    get_following(user)
