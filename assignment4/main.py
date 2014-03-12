from corpus import *
from eval import *
from taggers import *

if __name__ == "__main__":
	training_corpus = Corpus("data/train.txt")
	e = Evaluator()

	# Baseline tagger
	tagged_corpus = baseline_tagger(training_corpus, "data/development.txt", True)
	e.evaluate(tagged_corpus)
	e.print_stats()
	e.write_confusion_matrix("baseline_conf_m.txt")

	# Noisy channel tagger
	#tagged_corpus = noisy_channel_tagger(training_corpus, 'ex_sentence.txt', True, 8)
	tagged_corpus = noisy_channel_tagger(training_corpus, 'data/development.txt', True, 12)
	e.evaluate(tagged_corpus)
	e.print_stats()
	e.write_confusion_matrix("noisy_conf_m.txt")

	# Viterbi tagger
	tagged_corpus = viterbi_tagger(training_corpus, "data/development.txt", True)
	e.evaluate(tagged_corpus)
	e.print_stats()
	e.write_confusion_matrix("vitebri_conf_m.txt")

	# Viterbi tagger
	tagged_corpus = viterbi_tagger(training_corpus, "data/test.txt", False)
	tagged_corpus.write_conll("testset_tagged.txt")






