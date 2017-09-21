from lxml import html
import requests as r

url = 'http://www.ebuyer.com/store/Computer/cat/Gaming-Laptops'
urlx = '?page='
page = r.get(url)
tree = html.fromstring(page.content)

pages = str(tree.xpath('//*[@id="search-results"]/div[1]/div/ul/li[7]/text()'))
pages = int(pages.replace(' pages', '')[2]) + 1


for urls in range(2,pages):
    link = url + urlx + str(urls)
    print(link)





