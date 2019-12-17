#The program will prompt for a URL, read the JSON data from that URL using urllib and then
#parse and extract the comment counts from the JSON data, and compute the sum of the numbers in the file
import urllib.request, urllib.parse, urllib.error
import json

#Get the address
address = input('Enter location: ')
if len(address)<1:
    address='http://py4e-data.dr-chuck.net/comments_42.json'

#Open the web page, read its contents, and feed the contents into a string.
fhand=urllib.request.urlopen(address)
input=''
for line in fhand:
    inputpiece=line.decode().strip()
    input=input+inputpiece

#Create an object from the json
info=json.loads(input)
sum=0
lod=info["comments"]

#Loops through the dictionaries in the list and extracts the numbers, adds them to the sum
sum=0
for dic in lod:
    try:
        num=dic.get('count')
        sum=sum+num
#First item in the list has class list for some reason. This skips it.
    except:
        continue

print("Sum:", sum)

#Checking our work
sumstr=str(sum)
if sum==2553:
  print('Successful Test')
elif sumstr.endswith('3'):
  print('Success! Assignment complete.')
else:
  print('Something went wrong. Your sum was: ', sum, '. Go back and try something different.')
