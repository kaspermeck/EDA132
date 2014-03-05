# selects the most common output value among a set of examples
# input dataset
import random

def plurality_value(dataSet):
	p = 0
	n = 0
	attr = dataSet['attributes']
	index = len(attr)
	data = dataSet['data']
	yes_values = [True, 1, "yes", "ja", "true", "TRUE", "True"]
	for line in data:
		if line[index-1] in yes_values:
			p += 1
		else:
			n += 1

	if p == n:
		return bool(random.getrandbits(1))

	else:
		if p > n:
			return True
		else:
			return False