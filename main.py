#!/opt/imh-python/bin/python
import requests
from bs4 import BeautifulSoup

index = []
category_links = {}

r = requests.get('http://us.battle.net/sc2/en/profile/2950613/1/NDSCRMNTJSTC/achievements/')
text_res = r.text

#Choose to ignore Unicode like the (R) symbol (grrr, Blizzard)
soup = BeautifulSoup(text_res.encode('ascii','ignore'))

for link in soup.find_all('a'):
    if link.get('href').find('NDSCRMNTJSTC/achievements/category') != -1:
        index.append(link.get_text().strip())
        category_links[link.get_text().strip()] = link.get('href')

for i in index:
    print i
    print category_links[i]

#r = requests.get('http://us.battle.net'+category_links[index[0]])
#text_res = r.text
#
#soup = BeautifulSoup(text_res.encode('ascii','ignore'))
#
#print soup.prettify()
#for link in soup.find_all('div'):
#    print link
