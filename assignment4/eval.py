from corpus import *
from collections import *

class Evaluator(object):

  def __init__(self):
    self.accuracy = 0
    self.tags = {}

  def evaluate(self, tagged_corpus):
    tags = {}
    total_taggings = 0
    i = 0

    # Go through the tagged corpus and evaluate it
    for sentence in tagged_corpus.sentences:
      for line in sentence:
        i += 1
        POS = line['POS']

        # Make sure the tag is saved at least once
        if POS not in tags:
          tags[POS] = {}
          tags[POS]["accurate"] = 0
          tags[POS]["total"] = 0
          tags[POS]["error_pairs"] = []

        # If the POS equals PPOS, increase the accuracy count
        if POS == line['PPOS']:
          tags[POS]["accurate"] += 1
        else:
          tags[POS]["error_pairs"].append( (POS, line['PPOS']) )
          #print "ERROR: On line", i, "=>", line['PPOS'], "should be", POS

        # Increase the total times the POS has been seen
        tags[POS]["total"] += 1
        total_taggings += 1

    # Compute the accuracy
    accurate_sum = 0
    for tag in tags.values():
      accurate_sum += tag["accurate"]

    self.accuracy = float(accurate_sum)/total_taggings
    self.evaluated_tags = tags

  def print_stats(self, name, individual_tags = False):
    print "===== POS Tagger evaluation ============================="
    print "  Tagger:", name
    print "  Accuracy: %1.4f" % self.accuracy

    if individual_tags:
      print "  Accuracy for individual tags:"
      for POS, data in OrderedDict(sorted(self.evaluated_tags.items())).iteritems():
        print "       %(tag)-4s %(acc)1.3f" % \
              {"tag": POS, "acc": (float(data["accurate"])/data["total"])}

    print "========================================================="
    print ""

  def print_confusion_matrix(self, name):
    matrix = [[0 for key in self.tags.keys()] for key in self.tags.keys()]



if __name__ == "__main__":
  c = Corpus("data/train.txt")
  
  e = Evaluator()
  e.evaluate(c)
  e.print_stats("Test", True)
