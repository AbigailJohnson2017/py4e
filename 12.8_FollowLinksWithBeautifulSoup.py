import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
position=input('Position:')
index=int(position)-1
timesthrough=input('Repeat the process how many times?')
times=int(timesthrough)
# Retrieve all of the anchor tags
#Click Name Number 1
count=0
iteration=1
while iteration<=times:
    urls=list()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        newurl=tag.get('href', None)
        urls.append(newurl)
    url=urls[index]
    iteration=iteration+1
words=url.split('_')
name=words[2]
nameonly=name.split('.')
print('Name:', nameonly[0])
