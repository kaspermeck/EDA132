import operator, time
from corpus import *
def viterbi_tagger(training_corpus, file_to_tag):
	start_time = time.clock()

	# Create a corpus where we overwrite the PPOS
	tagged_corpus = Corpus(file_to_tag)
	tagged_corpus.training_file = training_corpus.corpus_file

	# Algorithm


	for sentence in tagged_corpus.sentences:

		# SETUP FIRST
		trellis = {}
		line = sentence[0] 
		POS = '<s>'

		trellis[POS] = {'value': 1, 'prev_path': None}
			
		# REST
		for line in sentence[1:]:
			word = line['FORM']
			
			if word not in training_corpus.POS_per_FORM:
				#1
				#total_words = training_corpus.total_words
				#s = sorted(training_corpus.POS.iteritems(), key=operator.itemgetter(1), reverse=True)
				#POSes_for_word = s[0]
			
				#2
				total_words = 1
				s = sorted(training_corpus.POS.iteritems(), key=operator.itemgetter(1), reverse=True)
				POS = s[0][0]
				POSes_for_words = {}
				POSes_for_words[POS] = 1
			else:
				POSes_for_word = training_corpus.POS_per_FORM[word][0]
				total_words = training_corpus.POS_per_FORM[word][1]
			
			trellis_new = {}
			for POS, count in POSes_for_word.iteritems():
				# P(word|ti)
				P_word_given_POS = float(count) / total_words
				
				# All P(ti|ti-1)
				P_POS_given_prevPOS = {}
				for prev_POS in trellis:
					value = trellis[prev_POS]['value']
					bigram = prev_POS + "++" + POS
					if bigram in training_corpus.bigrams:
						P_bigram = float(training_corpus.bigrams[bigram]) / training_corpus.POS[prev_POS]
					else:
						P_bigram = 0.01

					P_value = value*P_bigram
					P_POS_given_prevPOS[prev_POS] = P_value

				# P(word|ti) * max(P(ti|ti-1)
				maxBigram = max(P_POS_given_prevPOS)
				maxBigram = sorted(P_POS_given_prevPOS.iteritems(), 
										key=operator.itemgetter(1), reverse=True)
				
				P_word_given_POS *= maxBigram[0][1]
				prev_POS_used = maxBigram[0][0]

				#Save the data
				trellis_new[POS] = {}
				trellis_new[POS]['value'] = P_word_given_POS
				trellis_new[POS]['prev_path'] = {prev_POS_used: trellis[prev_POS_used]}
		
			# End of line: overwrite trellis	
			trellis = trellis_new

		# End of sentence: assign PPOS for sentence
		#for key, value in trellis.iteritems():
		#	print "POS for last word", key, "P()", value['value']

		s = sorted(trellis.iteritems(), key=lambda item: item[1], reverse=True)

		#print "SORTED YEEEEEEEEEEEEEEEEEEEAAAAAAAAAAAAAAAHHHHHHHHH"
		#for pair in s:
		#	print "POS for last word", pair[0], "P()", pair[1]['value']

		prev_path = {s[0][0]: s[0][1]}
		ID = sentence[-1]['ID']
		
		#print 'prev_path=', prev_path, 'id=', ID, 'POS=', POS
		#print prev_path

		while prev_path != None:
			POS = prev_path.keys()[0]
			sentence[ID]['PPOS'] = POS
		#	print 
		#	print "==== Word:", sentence[ID]['FORM']
		#	print "Predicted:", POS
		#	print "Should be:", sentence[ID]['POS']

			prev_path = prev_path[POS]['prev_path']
			ID -= 1
		

	tagged_corpus.time_elapsed = time.clock() - start_time
	return tagged_corpus

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


if __name__ == "__main__":
	c = Corpus("data/train.txt")
	baseline_tagger(c, "data/development.txt")
