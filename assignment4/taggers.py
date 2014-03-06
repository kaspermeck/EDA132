import operator, time
from corpus import *

def baseline_tagger(training_corpus, file_to_tag):
	start_time = time.clock()
	
	# Create a corpus where we overwrite the PPOS
	tagged_corpus = Corpus(file_to_tag)
	tagged_corpus.training_file = training_corpus.corpus_file


	# Baseline algortihm:
	# Tag using the most common POS for that word.
	
	def most_common_POS(word, corpus):
		if word in corpus.POS_per_FORM:
			# Return the most common POS for the word given				
			POSes = corpus.POS_per_FORM[word][0]
			#POSes = dict(POSes) # make a copy
			#del POSes['total']
			s = sorted(POSes.iteritems(), key=operator.itemgetter(1), reverse=True)
			return s[0][0] # s[most common POS][POS name]
		else:
			# Return the most common POS overall
			s = sorted(corpus.POS.iteritems(), key=operator.itemgetter(1), reverse=True)
			return s[0]


	for sentence in tagged_corpus.sentences:
		for line in sentence:
			word = line['FORM']
			
			# Set predicted POS
			line['PPOS'] = most_common_POS(word, training_corpus)
	
	tagged_corpus.time_elapsed = time.clock() - start_time
	return tagged_corpus

def viterbi_tagger(training_corpus, file_to_tag):
	start_time = time.clock()

	# Create a corpus where we overwrite the PPOS
	tagged_corpus = Corpus(file_to_tag)
	tagged_corpus.training_file = training_corpus.corpus_file

	# Algorithm


	for sentence in tagged_corpus.sentences:
		sent = []

		# FIRST
		line = sentence[1] 
		word = line['FORM'] #That

		ppf = training_corpus.POS_per_FORM[word]
		POSes = ppf[0]
		total = ppf[1]
		prev_POS = "<s>"
		sent.append({})

		for POS, value in POSes.iteritems():
			bigram = prev_POS + "++" + POS
			bigram_freq = training_corpus.bigrams[bigram] / training_corpus.POS[prev_POS]

			sent[0][POS] = float(value) / total * bigram_freq 

			
		# REST


	return tagged_corpus

if __name__ == "__main__":
	c = Corpus("data/train.txt")
	baseline_tagger(c, "data/development.txt")
