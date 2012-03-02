import random

def randommovie():
	content=open('movies.txt')
	content.seek(0)
	movies=[]
	for line in content.readlines():
		line=line.strip('\n')
		movies.append(line)
	return random.choice(movies)


