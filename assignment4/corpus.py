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
		self.POSBOS = self.get_number_of_POS_in_BOS()
		self.bigrams = self.get_bigrams()

	def extract_words(self):
		with open(self.corpusfile) as f:
			content = f.readlines()
		f.close()

		words = {}

		for line in content:
			line = line.split()
			if line:
				FORM = line[1]
				POS = line[5]
				if FORM not in words:
					words[FORM] = {}
				if POS not in words[FORM]:
					words[FORM][POS] = 1
					words[FORM]['total'] = 1
				else:
					words[FORM][POS] += 1
					words[FORM]['total'] += 1

		return words

	def extract_sentences(self):
		with open(self.corpusfile) as f:
			content = f.readlines()
		f.close()

		sentences = []
		sentence = [{'ID':0,'FORM':'<s>','POS':'<s>'}]
		row = {}

		for line in content:
			line = line.split()
			# check if empty line => new sentence
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

	def get_number_of_POS_in_BOS(self):
		BOS = {'total':0}

		for sentence in self.sentences:
			firstPOS = sentence[1]['POS']
			BOS['total'] += 1

			if firstPOS not in BOS:
				BOS[firstPOS] = 1
			else:
				BOS[firstPOS] += 1

		return BOS

	def get_bigrams(self):
		# a bigram is how many times POS1 comes before POS2
		# it will be named: POS1|POS2

		with open(self.corpusfile) as f:
			content = f.readlines()
		f.close()

		bigram = {'total': 0}
		return bigram
"""
		POScol = []

		for line in content:
			line = line.split()
			if line:
				POScol.append(line[4])
			if not line:
				for POS in POScol[1:]:
					if POS


				POScol = []
"""







if __name__ == '__main__':
	corp = Corpus('./data/train.txt')
	print "len sentences : ", len(corp.sentences)
	print "len words: ", len(corp.words)
	print "len POSBOS: ", len(corp.POSBOS)
