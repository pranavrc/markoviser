'''
Created on Nov 28, 2011

@author: root
'''

import urllib2
from BeautifulSoup import BeautifulSoup
import re
import markov
import movielist
import random 
import socket


def returnmarkovised():
	final = []

	while 1:
		try:
			randommoviename=movielist.randommovie()
			url='http://www.moviequotedb.com/movies/'+randommoviename+'.html'
			print url
			socket.setdefaulttimeout(3)
			contents = urllib2.urlopen(url)
		except urllib2.URLError:
			continue
		break
	soup = BeautifulSoup(contents);

	soup1 = soup.findAll(id=re.compile('quote'))

	for row in soup1:
	    text = ''.join(row.findAll(text=True))
	    data = text.strip()
	    final.append(data)

	file = open('wordlist.html', 'w')

	linecount={}
	values=[]
	lengthiest=[]

	for item in final:
	    count=item.count('\n')
	    linecount.setdefault(item, count)
	    values.append(count)

	for j in range(1,6):
		maximum=[k for k, v in linecount.iteritems() if v == max(i for i in values)][0]
		lengthiest.append(maximum)
	originaltext=random.choice(lengthiest)
	file.write("%s\n" % originaltext.encode('utf-8'))
	file.close()

	markovisedtext=markov.markovify()
	
	originaltext=originaltext.replace('\n','<br />')
	markovisedtext=markovisedtext.replace('\n','<br />')
	try:
		return "<h3>Quote</h3>"+originaltext+"<br /><hr />"+"<h3>Markovised</h3>"+markovisedtext.encode('utf-8')+"<hr />"+"<h3>Movie</h3>"+(randommoviename.encode('utf-8')).replace('-',' ')
	except UnicodeDecodeError:
		returnmarkovised()

if __name__=="__main__":
	returnmarkovised()
