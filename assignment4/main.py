from corpus import *
from eval import *
from taggers import *

if __name__ == "__main__":
	training_corpus = Corpus("data/train.txt")
	test_file = "data/development.txt"
	e = Evaluator()

	# Baseline tagger
	tagged_corpus = baseline_tagger(training_corpus, test_file)
	e.evaluate(tagged_corpus)
	e.print_stats("Baseline", True)

	# Viterbi tagger
	tagged_corpus = viterbi_tagger(training_corpus, test_file)
	e.evaluate(tagged_corpus)
	e.print_stats("Vitebri", True)


