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
  # Compute the gain of the attribute
  gain = False
  size = len(dataset['data'])

  for attr_pos, (attr_name, attr_values) in enumerate(dataset['attributes']):
    if attr != attr_name:
      continue

    gain = 1.0
    for attr_value in attr_values:
      pos = 0
      neg = 0
      for data in dataset['data']:
        if data[attr_pos] == attr_value:
          if data[-1]:
            pos += 1
          else:
            neg += 1
      if pos+neg > 0:
        gain -= (pos+neg)/size * Bfun(pos/(pos+neg))

  return gain

def Bfun(q):
  val = 0
  if q > 0:
    val += q*log(q, 2)
  if 1-q > 0:
    val += (1-q)*log(1-q, 2)
  return -val


#if __name__ == "__main__":
#  print importance(ex_dataset, "outlook"), importance(ex_dataset, "wind")


