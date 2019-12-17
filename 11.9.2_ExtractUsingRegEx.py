import re
file=input('File:')
hand=open(file)
sum=0
count=0
for line in hand:
    line=line.rstrip()
    snums=re.findall('[0-9]+', line)
    for thing in snums:
        fnum=int(thing)
        sum=sum+fnum
        count=count+1
print('Sum:', sum)
print('Count:', count)
