import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import re

address = input('Enter location: ')

fhand=urllib.request.urlopen(address)
input=''
for line in fhand:
    inputpiece=line.decode().strip()
    input=input+inputpiece

#Find the sum of all the count tags in whatever xml string is saved as input
#Don't fuck with anything below this line!!
stuff = ET.fromstring(input)
lst=stuff.findall('.//comment')
sum=0
counts=0
for item in lst:
    number=item.find('count').text
    num=int(number)
    sum=sum+num
print('Sum:', sum)

sumstr=str(sum)
if sumstr.endswith('63'):
    print('Success!')
