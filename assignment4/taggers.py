import operator, time
from corpus import *


def noisy_channel_tagger(training_corpus, file_to_tag, readPOS, n):
	start_time = time.clock()
	
	# Create a corpus where we overwrite the PPOS
	tagged_corpus = Corpus(file_to_tag, readPOS)
	tagged_corpus.training_file = training_corpus.corpus_file
	tagged_corpus.tagger_name = "Noisy channel tagger"
	
	# Extract all sentences of length < n
	short_sentences = [x for x in tagged_corpus.sentences if len(x) < n]

	# Recursive function which uses hidden markov model
	def recursive(sentence, prev_POS, probability, n):
		if n == 0:
			#Reached end of sentence
			return {'value': probability, 'POS': []}
		else:
			word = sentence[0]['FORM'] # front word of the sentence

			# Extract POS list for current word
			if word in training_corpus.POS_per_FORM:
				ppf = training_corpus.POS_per_FORM[word]
				POSes = ppf[0]
				total_words = ppf[1]
			else:
				s = sorted(training_corpus.POS.iteritems(), key=operator.itemgetter(1), reverse=True)
				POSes = {s[0][0]: 1}
				total_words = 1

			best_path = {'value': 0}
			for POS, value in POSes.iteritems():
				P_word_given_POS = float(value) / total_words

				bigram = prev_POS + "++" + POS
				if bigram in training_corpus.bigrams:
					P_bigram = float(training_corpus.bigrams[bigram]) / training_corpus.POS[prev_POS]
				else:
					# quite low ?
					P_bigram = 0.01

				prob = P_word_given_POS * P_bigram

				path = recursive(sentence[1:], POS, probability*prob, n-1)

				if path['value'] > best_path['value']:
					best_path = path
					best_path['POS'].insert(0, POS)

			return best_path

	# Recursive call 
	for sentence in short_sentences:
		best_path = recursive(sentence, '<s>', 1, len(sentence))
		
		# Assign the computed POS tags to their words
		for i, line in enumerate(sentence):
			line['PPOS'] = best_path['POS'][i]

	# Save sentences
	tagged_corpus.sentences = short_sentences

	# Return the now tagged corpus
	tagged_corpus.time_elapsed = time.clock() - start_time
	return tagged_corpus



def viterbi_tagger(training_corpus, file_to_tag, readPOS):
	start_time = time.clock()

	# Create a corpus where we overwrite the PPOS
	tagged_corpus = Corpus(file_to_tag, readPOS)
	tagged_corpus.training_file = training_corpus.corpus_file
	tagged_corpus.tagger_name = "Viterbi tagger"

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
				P_word_given_POS = float(count) / training_corpus.POS[POS]#total_words
				
				# All P(ti|ti-1)
				P_POS_given_prevPOS = {}
				for prev_POS in trellis:
					value = trellis[prev_POS]['value']
					bigram = prev_POS + "++" + POS
					if bigram in training_corpus.bigrams:
						P_bigram = float(training_corpus.bigrams[bigram]) / training_corpus.POS[prev_POS]
					else:
						# quite low ?
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
		s = sorted(trellis.iteritems(), key=lambda item: item[1], reverse=True)

		prev_path = {s[0][0]: s[0][1]}
		ID = sentence[-1]['ID']

		while prev_path != None:
			POS = prev_path.keys()[0]
			sentence[ID]['PPOS'] = POS
			prev_path = prev_path[POS]['prev_path']
			ID -= 1

	tagged_corpus.time_elapsed = time.clock() - start_time
	return tagged_corpus

def baseline_tagger(training_corpus, file_to_tag, readPOS):
	start_time = time.clock()
	
	# Create a corpus where we overwrite the PPOS
	tagged_corpus = Corpus(file_to_tag, readPOS)
	tagged_corpus.training_file = training_corpus.corpus_file
	tagged_corpus.tagger_name = "Baseline tagger"

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
