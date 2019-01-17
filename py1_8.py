from lxml import etree

html_data = '''
<html>
<body>
<div class="first">
  <p class="name">Crossin</p>
  <p class="age">18</p>
</div>
<div class="second">
  <p class="name">Mike</p>
  <p class="age">20</p>
</div>
</body>
</html>
'''

root = etree.HTML(html_data)
print(root)
first = root.xpath('/html/body/div/p')
print(first)
print(root.xpath('div/p'))
# print(first.xpath('text()')[0])

# print(first.xpath('../div[@class="second"]'))
# print(first.xpath('./p[@class="name"]/text()'))
# print(first.xpath('./p/text()'))
# print(first.xpath('p/text()'))
# print(first.xpath('.//p/text()'))
# print(first.xpath('//p/text()'))
# print(first.xpath('/html'))
# print(first.xpath('html'))
# print(root.xpath('/html'))