from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ureq
'''
Scrapes IMDB Top movies, then copys to a file. This very rough around the edges but it works  
'''
for year in range(2010,2018):
    # Set URL with year var.
    url = 'http://www.imdb.com/search/title?year=%s,%s&title_type=feature&sort=moviemeter,asc' % (year, year)

    # set connections
    uclient = ureq(url)
    sauce = uclient.read()
    uclient.close()

    # Set parser
    soup = bs(sauce, 'html.parser')

    # Set CSV name  and headers
    fn = 'Top_Movies %s.csv' % str(year)
    header = 'Title, Cert, Rating, Votes, Runtime, Genre\n'
    f = open(fn, "w")
    f.write(header)

    # loop though all Html objects and strip, convert and clean
    containers = soup.find_all('div', {'class': 'lister-item-content'})
    for contain in containers:
        title = contain.find_all('a')[0].text
        try:
            cert = contain.find_all('span', {'class': 'certificate'})[0].text
        except Exception:
            cert = 'NA'
        try:
            rating = contain.find_all('div', {'class': 'ratings-imdb-rating'})[0].text
        except Exception:
            rating = 0.0
        rating = str(rating)
        try:
            votes = contain.find_all('span', {'name': 'nv'})[0].text
        except Exception:
            votes = 0
        try:
            runtime = contain.find_all('span', {'class': 'runtime'})[0].text
        except Exception:
            runtime = 'Unknown'
        try:
            genre = contain.find_all('span', {'class': 'genre'})[0].text
        except Exception:
            genre = 'NA'
        f.write(title + ',' + cert + ',' + str(rating).strip() + ',' +
                str(votes).replace(',', '') + ',' + runtime + ',' + genre.replace(',', ' |').strip() + ',\n')

    f.close()