import urllib
import re
import bs4 as bs
url="https://en.wikipedia.org/wiki/Ram_Charan"
hand=urllib.request.urlopen(url)
ht=hand.read()
txt=bs.BeautifulSoup(ht,'html.parser')
x=""
for s in txt.find_all('p'):
    x=x+str(s.text)
for i in x.split('.'):
    print(i)