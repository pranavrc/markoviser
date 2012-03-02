#!/usr/bin/env python
import random

class Markov:
    def __init__(self, file, size):
        self.size = size
        self.starts = []
        self.cache = {}
        self.file_to_words(file)
        self.parse_words()

    def file_to_words(self, file):
        file.seek(0)
        data = file.read()
        self.words = data.split("\n")


    def tuples(self, word):
        if len(word) < self.size - 1:
            return

        word = word + "\n"

        for i in range(len(word) - self.size):
            yield (word[i:i + self.size], word[i + self.size])


    def parse_words(self):
        for word in self.words:
            self.starts.append(word[:self.size])
            for key, next in self.tuples(word):
                if key in self.cache:
                    self.cache[key].append(next)
                else:
                    self.cache[key] = [next]
	for i in self.starts[:]:
		if i=='' or i=='\r':
			self.starts.remove(i)
	
	

    def generate_word(self):
        key = random.choice(self.starts)
        word = key
        next = random.choice(self.cache[key])
        while next != "\n":
            word = word + next
            key = key[1:] + next
	    while 1:
		 try:
		      next = random.choice(self.cache[key])
		 except KeyError:
		      continue
	      	 break	
        return word

from optparse import OptionParser

def markovify():
    generatedword=''	
    parser = OptionParser()
    parser.add_option('-p', type='int', dest='prev_num', default=3,
                      help='number of previous letters to base chain on')
    parser.add_option('-n', type='int', dest='num', default=5,
                      help='number of generated words')
    parser.add_option('-s', '--source-text', type='string',
                      default='wordlist.html', dest='source',
                      help='file to use as basis for generating the words')
    (options, args) = parser.parse_args()

    file = open(options.source)
    markov = Markov(file, options.prev_num)
    file.close()
    for i in range(options.num):
        generatedword=generatedword+markov.generate_word()+'\n'
    return generatedword	

if __name__ == '__main__':
    markovify()


