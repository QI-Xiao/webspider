from lxml import etree

html_data ="""
<section>
    <article class='python'>
        <h3>The Zen of Python</h3>
        <p class='English'>
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
        </p>
    </article>
    <article class='python'>
        <h3>Python 之禅</h3>
        <p class='Chinese'>
Python 之禅，by Tim Peters
优美胜于丑陋
明确胜于隐晦
简单胜于复杂
复杂胜于凌乱
扁平胜于嵌套
稀疏胜于紧凑
可读性至关重要
即便特例，也需服从以上规则
除非刻意追求，错误不应跳过
面对歧义条件，拒绝尝试猜测
解决问题的最优方法应该有且只有一个
尽管这一方法并非显而易见（除非你是Python之父）
动手胜于空想
空想胜于不想
难以解释的实现方案，不是好方案
易于解释的实现方案，才是好方案
命名空间是个绝妙的理念，多多益善！
        </p>
    </article>
</section>
"""

# xp = etree.HTML(html_data)
# article = xp.xpath('//p')[0]
# print(article.text)


with open('baidu.html', encoding="utf-8") as f:
    content = f.read()
    print(content)
html = etree.HTML(content)
ps = html.xpath('//p')
print(ps)
for p in ps:
    with open('new.txt'.format(ps.index(p)),'w') as f:
        print(ps.index(p), p.text)
        f.write(p.text.encode('utf8'))