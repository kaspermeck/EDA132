import timeit

class Corpus(object):
	def __init__(self, corpus_file, readPOS = True):
		self.corpus_file = corpus_file
		self.readPOS = readPOS
		self.sentences = self.extract_sentences()
		
		if readPOS:		
			self.POS = self.extract_POS()
			self.POS_per_FORM = self.extract_POS_per_FORM()
			self.bigrams = self.extract_bigrams()
		

	def extract_POS_per_FORM(self):
		words = {}

		for sentence in self.sentences:
			for line in sentence: 
				POS = line['POS']
				FORM = line['FORM']

				if FORM not in words:
					words[FORM] = [{}, 0]
					#words[FORM] = {'total': 0}
				
				if POS not in words[FORM][0]:
					words[FORM][0][POS] = 1
				else:
					words[FORM][0][POS] += 1
				
				words[FORM][1] += 1

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
				row['ID'] = int(line[0])
				row['FORM'] = line[1]
				if self.readPOS:
					row['POS'] = line[4]
					row['PPOS'] = line[5]

				sentence.append(row)

		# Add last sentence
		sentences.append(sentence)

		return sentences

	def extract_bigrams(self):
		# A bigram is all a tuple (POS(i-1), POS(i)), i.e. previous POS followed
		# by the current POS.
		# A bigram is represented as a (key:value) pair: ("POS1++POS2":n)

		bigrams = {}
		prev_POS = "<s>"

		for sentence in self.sentences[1:]:
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

	def write_conll(self, filename):
		text_file = open(filename, "w")

		print_string = ""
		for sentence in self.sentences:
			for line in sentence[1:]:
				print_string += `line['ID']` + "\t" +  line['FORM'] + "\t" + line['PPOS'] + "\n"
			print_string += "\n"
		print_string = print_string[:-2] #trim last newline

		text_file.write(print_string)
		text_file.close()

	


if __name__ == '__main__':
	stmt = "corp = Corpus('./ex_sentence.txt')"
	time = timeit.timeit(stmt, setup="from __main__ import Corpus", number=1)

	print "Time spent reading corpus:", time
#	print "len sentences : ", len(corp.sentences)
	#print "len words: ", len(corp.words)
	#print "len POSBOS: ", len(corp.POSBOS)
