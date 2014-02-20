from __future__ import division
from math import log

# Example dataset
ex_dataset = {'relation':   "weather", 
              'attributes': [("outlook", ("sunny", "rainy", "foggy")),
                             ("wind", (True, False)),
                             ("play", (True, False))],
              'data':       [("sunny", False, True),
                             ("rainy", False, True),
                             ("rainy", True, False),
                             ("sunny", True, True)]}


# Return a gain value for a given attribute in the given dataset
def importance(dataset, attr):
  gain = False
  size = len(dataset['data'])
  yes_values = [True, 1, "yes", "ja", "true", "TRUE", "True"]

  for attr_pos, (attr_name, attr_values) in enumerate(dataset['attributes']):
    # Check if the current attribute is the one we want to compute gain for
    if attr != attr_name:
      continue

    # Compute gain
    gain = 1.0
    for attr_value in attr_values: 
      pos = neg = 0
      for data in dataset['data']:
        if data[attr_pos] == attr_value:
          # Assign the boolean value from the last column as pos or neg
          if data[-1] in yes_values:
            pos += 1
          else:
            neg += 1
      # Subtract the gain if we had any attr_value assigned in the dataset
      # print "Got pos =", pos, "and neg =", neg, "for", attr_value
      if pos+neg > 0:
        gain -= (pos+neg)/size * Bfunc(pos/(pos+neg))

  # gain will be False it attr was not found in the dataser,
  # otherwise it will be the gain.
  return gain

def Bfunc(q):
  # val = -(q*log(q) + (1-q)*log(1-q))
  val = 0
  if q > 0:
    val += q*log(q, 2)
  if 1-q > 0:
    val += (1-q)*log(1-q, 2)
  return -val


#if __name__ == "__main__":
#  print importance(ex_dataset, "outlook"), importance(ex_dataset, "wind")


