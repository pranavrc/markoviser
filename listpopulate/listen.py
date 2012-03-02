import urllib2
from BeautifulSoup import *
final=[]
readstring=''


content=open('list.txt')

for line in content.readlines():
	readstring=readstring+line

#print readstring

soupped=BeautifulSoup(readstring)

extext=soupped.findAll('a',href=re.compile('http'))

for row in extext:
	text = ''.join(row.findAll(text=True))
	final.append(text)

for i in range(len(final)):
	final[i]=final[i].replace(' ','-')
	print final[i]

print final

