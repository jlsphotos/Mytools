from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ureq

url = 'http://www.imdb.com/search/title?year=2017,2017&title_type=feature&sort=moviemeter,asc'

# set connections
uclient = ureq(url)
sauce = uclient.read()
uclient.close()

# Set parcer
soup = bs(sauce, 'html.parser')

# Set CSV
fn = 'Top_Movies.csv'
header = 'Title,'
f = open(fn, "w")

containers = soup.find_all('div',{'class':'lister-item-content'})
for contain in containers:

    title = contain.find_all('a')[0].text
    try:
        cert = contain.find_all('span',{'class':'certificate'})[0].text
    except Exception:
        cert = 'NA'

    try:
        rating = contain.find_all('div',{'class':'ratings-imdb-rating'})[0].text
    except Exception:
        rating = 0.0

    try:
        votes = contain.find_all('span',{'name':'nv'})[0].text
    except Exception:
        votes = 0

    try:
        runtime = contain.find_all('span', {'class':'runtime'})[0].text
    except Exception:
        runtime = 'Unknown'

    try:
        genre = contain.find_all('span', {'class': 'genre'})[0].text
    except Exception:
        genre = 'NA'

    print(cert,title,rating,votes,runtime,genre.replace(',','|'))






# fn = 'top_movies.csv'
# f = open(fn,"w")
# header = 'Id, Title, Rating, Meta, Desc,Director, Votes, Gross\n'
#
# f.write(header)
#
#
# #This will create a list of buyers:
#
# ids = [x.strip('.') for x in tree.xpath('//*[@id="main"]/div/div/div[3]/div/div[3]/h3/span[1]/text()')]
# titles = tree.xpath('//*[@id="main"]/div/div/div/div/div/h3/a/text()')
# ratings = tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/div/div[1]/strong/text()')
# metas = [x.strip(' ') for x in tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/div/div[3]/span/text()')]
# descs = tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/p[2]/text()')
# directors = tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/p[3]/a[1]/text()')
# votess = tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/p[4]/span[2]/text()')
# grosss = tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/p[4]/span[5]/text()')
#
# for id, title, rating,meta,desc,director, votes,gross in ids,titles,ratings,metas,descs,directors,votess,grosss:
#     f.write(id + ',' + title + ',' + rating + ',' + meta + ',' + desc.replace("," , "|") + ',' + director + ',' + votes + ',' + gross)
#
# f.close()
#
# # print(id)
# # print(title)
# # print(rating)
# # print(meta)
# # print(desc)
# # print(director)
# # print(votes)
# # print(gross)
#
#
