import requests
from lxml import etree

url = 'http://jandan.net/duan'
data_all = ''
for page in range(3):
    req = requests.get(url)
    html = req.text
    # print(req.encoding)

    tree = etree.HTML(html)
    # print(tree)
    result = tree.xpath('//li//div[@class="text"]')
    print(result)

    for div in result:
        author = div.xpath('../div[@class="author"]/strong/text()')
        print(author[0])
        data_all += (author[0] + ':\n')
        content = div.xpath('p/text()')
        for p in content:
            print(p)
            data_all += p
        print('============')
        data_all += '\n\n'

    current_page = tree.xpath('//span[@class="current-comment-page"]/text()')
    next_page = int(current_page[0].strip('[]')) - 1
    url = 'http://jandan.net/duan/page-%d' % next_page
    # print('PAGE:', next_page, url)

with open('jocks.txt', 'w', encoding='utf-8') as f:
    f.write(data_all)

# xml_data = '<html><body><root>data</root></body></html>'
# root = etree.HTML(xml_data)
# print(root)
# print(root.tag)
# print(etree.tostring(root))
# root.xpath('//text()')