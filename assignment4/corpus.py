import timeit
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
	def __init__(self, corpus_file):
		self.corpus_file = corpus_file
		self.sentences = self.extract_sentences()
		
		self.POS = self.extract_POS()
		self.POS_per_FORM = self.extract_POS_per_FORM()
		self.bigrams = self.extract_bigrams()

		#self.words = self.extract_words()
		#self.POSBOS = self.get_number_of_POS_in_BOS()
		#for POS, val in self.POSBOS.iteritems():
		#	print POS, val
		

	def extract_POS_per_FORM(self):
		words = {}

		for sentence in self.sentences:
			for line in sentence: 
				POS = line['POS']
				FORM = line['FORM']

				if FORM not in words:
					words[FORM] = {'total': 0}
				
				if POS not in words[FORM]:
					words[FORM][POS] = 1
				else:
					words[FORM][POS] += 1
				
				words[FORM]['total'] += 1

		return words

	def extract_POS(self):
		POSes = {}

		for sentence in self.sentences:
			for line in sentence:
				POS = line['POS']

				if POS not in POSes:
					POSes[POS] = 1
				else:
					POSes[POS] += 1
		
		return POSes

	def extract_sentences(self):
		with open(self.corpus_file) as f:
			content = f.readlines()
		f.close()

		# The row used for beginning of sentences
		BOS_row = {'ID':0, 'FORM':'<s>', 'POS':'<s>', 'PPOS':'<s>'}

		sentences = []
		sentence = []
		sentence.append(BOS_row)

		for line in content:
			line = line.split()

			# check if empty line => new sentence
			if not line:
				sentences.append(sentence)
				sentence = []
				sentence.append(BOS_row)
			else:
				row = {}
				row['ID'] = line[0]
				row['FORM'] = line[1]
				row['POS'] = line[4]
				row['PPOS'] = line[5]
				sentence.append(row)

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

	def extract_bigrams(self):
		# A bigram is all a tuple (POS(i-1), POS(i)), i.e. previous POS followed
		# by the current POS.
		# A bigram is represented as a (key:value) pair: ("POS1++POS2":n)

		bigrams = {}
		prev_POS = "<s>" # initial POS hack

		for sentence in self.sentences:
			for line in sentence:
				POS = line['POS']
				bigram_name = prev_POS + "++" + POS
				
				# Search for bigram and insert it
				if bigram_name not in bigrams:
					bigrams[bigram_name] = 1
				else:
					bigrams[bigram_name] += 1

				# Update previous POS
				prev_POS = POS

		return bigrams



if __name__ == '__main__':
	stmt = "corp = Corpus('./data/train.txt')"
	time = timeit.timeit(stmt, setup="from __main__ import Corpus", number=1)

	print "Time spent reading corpus:", time
#	print "len sentences : ", len(corp.sentences)
	#print "len words: ", len(corp.words)
	#print "len POSBOS: ", len(corp.POSBOS)
