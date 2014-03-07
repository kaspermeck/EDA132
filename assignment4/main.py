from corpus import *
from eval import *
from taggers import *

if __name__ == "__main__":
	training_corpus = Corpus("data/train.txt")
	test_file = "data/development.txt"
	e = Evaluator()

	# Baseline tagger
	tagged_corpus = baseline_tagger(training_corpus, "data/development.txt", True)
	e.evaluate(tagged_corpus)
	e.print_stats()

	# Noisy channel tagger
	#tagged_corpus = noisy_channel_tagger(training_corpus, 'ex_sentence.txt', True, 8)
	tagged_corpus = noisy_channel_tagger(training_corpus, 'data/development.txt', True, 8)
	e.evaluate(tagged_corpus)
	e.print_stats()

	# Viterbi tagger
	tagged_corpus = viterbi_tagger(training_corpus, "data/development.txt", True)
	e.evaluate(tagged_corpus)
	e.print_stats()



	
	# Viterbi tagger
	#tagged_corpus = viterbi_tagger(training_corpus, test_file)
	#e.evaluate(tagged_corpus)
	#e.print_stats("Vitebri", False)

	# Viterbi tagger
	#tagged_corpus = viterbi_tagger(training_corpus, "data/test.txt")
	#e.evaluate(tagged_corpus)
	#e.print_stats("Vitebri", False)






