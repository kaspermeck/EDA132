"""
extracts a list of distinct words and 
their frequencies from a training set.
Extracts a list of distinct parts of 
speech (POS) and their frequencies 
from a training set.

self.sentences = 
[
[{'ID':n, 'FORM':'word', 'POS':'pos'}],
[{'ID':n, 'FORM':'word', 'POS':'pos'}],
...,
[{'ID':n, 'FORM':'word', 'POS':'pos'}]
]

self.words =
{
'word1' : {'total':n, 'POS1':m, ..., 'POSL':l},
'word2' : {'total':n, 'POS1':m, ..., 'POSL':l},
...,
'wordLAST' : {'total':n, 'POS1':m, ..., 'POSL':l}
}

"""

class Corpus(object):
	"""
	takes a corpus trainingset as input
	"""
	def __init__(self, corpusfile):
		# the traning file
		self.corpusfile = corpusfile
		self.sentences = self.extract_sentences()
		self.words = self.extract_words()

	def extract_words(self):
		# the dictionary with all words
		words = {}

		for sentence in self.sentences:
			for dictword in sentence:
				# get word and its POS
				word = dictword['FORM']
				wordPOS = dictword['POS']

				# word already exists
				if word in words.keys():
					# POS type exists, add one to count
					if wordPOS in words[word].keys():
						words[word][wordPOS] += 1

					else:
						words[word][wordPOS] = 1

					words[word]['total'] += 1

				# word doesn't exist, add
				else:
					# add word and a list of 'total' and POS
					words[word] = {'total' : 1, wordPOS : 1}

		return words

	def extract_sentences(self):
		with open(self.corpusfile) as f:
			content = f.readlines()
		f.close()

		sentences = []

		sentence = [{'ID':0,'FORM':'<s>','POS':'<s>'}]
		row = {}
		for line in content:
			# check if empty line => new sentence
			line = line.split()
			if not line:
				sentences.append(sentence)
				# break; USE BREAK TO CHECK IF CORRECT
				sentence = [{'ID':0,'FORM':'<s>','POS':'<s>'}]

			else:
				row['ID'] = line[0]
				row['FORM'] = line[1]
				row['POS'] = line[4]
				sentence.append(row)
				row = {}

		return sentences

if __name__ == '__main__':
	corp = Corpus('./data/train.txt')
	print "print sentences : ", corp.sentences
	print "print words: ", corp.words
