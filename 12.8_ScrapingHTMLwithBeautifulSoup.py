import urllib.request, urllib.parse, urllib.error

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

url=input('Enter url - ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

sum=0
tags=soup('span')
for tag in tags:
    num=tag.contents[0]
    sum=sum+int(num)
print(sum)
