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
    #print selectedList, '\n' ,'gain :', gain, ' attribute :', attr_name

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


def compute_split_points_for_reals(dataset):
  data = dataset['data']
  attributes = dataset['attributes']
  
  for column, attr in enumerate(attributes):
    if not 'real' in attr[1]:
      continue
    
    # sort the list after value
    data.sort(key=lambda x: x[column])

    # find split point
    gains = []
    for index, item in enumerate(data):
      # skip the first value (no split at index zero
      if index == 0:
        continue

      if item[-1] != data[index-1][-1]:
        # convert list
        converted_data = list(data)
        for i, line in enumerate(converted_data):
          if i < index:
            line[column] = 'low'
          else:
            line[column] = 'high'

        # create selected list
        sel_lst = getSelectedList(dataset, column)
    
        # split
        gain = getGain(sel_lst, ('low', 'high'))
        gains.append([index, gain])

    maxGain = max(gains, key=lambda x: x[1])
    split = maxGain[0]

    # convert data
    for i, line in enumerate(data):
      if i < split:
        line[column] = 'low'
      else:
        line[column] = 'high'

    # convert attribute
    attributes[column][1] = ('low', 'high')

  # return dataset
  return dataset

if __name__ == "__main__":
  print importance(ex_dataset, "outlook"),'\n', importance(ex_dataset, "wind")
