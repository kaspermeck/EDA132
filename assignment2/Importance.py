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

yes_values = [True, 1, "yes", "ja", "true", "TRUE", "True", "democrat"]

# return a gain value for a given attribute in the given dataset
def importance(dataset, attr):
  gain = False
  size = len(dataset['data'])

    # we know the attribute is in the dataset, now we need to find it
  for attr_pos, (attr_name, attr_values) in enumerate(dataset['attributes']):
    # Check if the current attribute is the one we want to compute gain for
    if attr != attr_name:
      continue
    
    selectedList = getSelectedList(dataset, attr_pos)

    gain = getGain(selectedList, attr_values)
    print selectedList, '\n' ,'gain :', gain, ' attribute :', attr_name

  # nothing found return false
  return gain

def getSelectedList(dataset, attr_pos):
  # extracts the value according to attribute with yes/no values
  selectedList = []
  for dataline in dataset['data']:
    selectedList.append([dataline[attr_pos], dataline[-1]])

  return selectedList

def getGain(selectedList, attr_values):
  gain = 1
  size = len(selectedList)
  if (isInt(selectedList[0][0])):
    selectedList, attr_values = convert_from_int(selectedList)

  for attr in attr_values:
    pos = neg = 0
    for line in selectedList:
      if attr == line[0]:
        # Assign the boolean value from the last column as pos or neg
        if line[-1] in yes_values:
          pos += 1
        else:
          neg += 1
        # Subtract the gain if we had any attr_value assigned in the dataset
        # print "Got pos =", pos, "and neg =", neg, "for", attr_value
        gain -= (pos+neg)/size * Bfunc(pos/(pos+neg))

  # gain will be False it attr was not found in the dataser,
  # otherwise it will be the gain.
  return gain

def convert_from_int(selectedList):
  # sort the list after size
  selectedList.sort()
  # find a number to "cut at"
  size = len(selectedList)
  weight = 0
  for value in selectedList:
    weight += value[0]
  weight /= size

  # set integers to low/high according to weight
  newList = []
  for value in selectedList:
    if value[0] < weight:
      newList.append(['low', value[-1]])
    else:
      newList.append(['high', value[-1]])

  print newList
  
  return newList, ['low', 'high']

def Bfunc(q):
  # val = -(q*log(q) + (1-q)*log(1-q))
  val = 0
  if q > 0:
    val += q*log(q, 2)
  if 1-q > 0:
    val += (1-q)*log(1-q, 2)
  return -val

def isInt(q):
  try:
    int(q)
    return True
  except ValueError:
    return False

if __name__ == "__main__":
  print importance(ex_dataset, "outlook"),'\n', importance(ex_dataset, "wind")
