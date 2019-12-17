# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
lst=list()
for line in handle:
    if not line.startswith('From '):
        continue
    words=line.split()
    time=words[5]
    nums=time.split(':')
    hour=nums[0]
    counts[hour]=counts.get(hour, 0)+1
lst=sorted(counts.items())
for h,c in lst:
    print(h, c)
