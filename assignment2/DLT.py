from plurality_value import plurality_value as p_val
from Importance import importance as gain
import copy
from tree import Node as Node

def DLT(dataset, parent_dataset):

  if not dataset['data']:
    if not parent_dataset:
      return ''
    else:
      node = Node()
      node.answer = p_val(parent_dataset)
      return node

  # creates an array with all the last column data values
  data = dataset['data']
  dataLastCol = []
  for line in data:
    dataLastCol.append(line[-1])

  if all(x == dataLastCol[0] for x in dataLastCol):
    node = Node()
    # all values are the same in dataLastCol, choose any index
    node.answer = dataLastCol[0]
    return node
  
  elif not dataset['attributes']:
    # if there are no attributes left in the dataset
    node = Node()
    node.answer = p_val(dataset)
    return node
  
  else:
    #print "We are in the else case!"
    
    # Find max gain
    gains = []
    attributes = dataset['attributes']
    for attr in attributes[:-1]:
      gains.append(gain(dataset, attr[0]))

    max_attr_index = gains.index(max(gains))
    max_attr = attributes[max_attr_index]
    
    # Create a new new for the tree
    node = Node()
    node.attribute = max_attr[0]

    # Clone the attributes list but remove the current attribute
    attributes_new = []
    for attr in attributes:
      if attr != max_attr:
        attributes_new.append(attr)

    # Branch the values
    for attr_value in max_attr[1]:
      data_new = []

      # Clone the data for the chosen attribute
      for dataLine in data:
        if dataLine[max_attr_index] == attr_value:
          d = list(dataLine) # copy the tuple to a new list
          #print "removing", max_attr_index, "from", d
          del d[max_attr_index] # remove the current attribute
          data_new.append(tuple(d))

      # Create the branched dataset
      branched_dataset = {}
      branched_dataset['attributes'] = attributes_new
      branched_dataset['data'] = data_new

      # Create the subtree/child
      child = DLT(branched_dataset, dataset) #DLT(dataset, parent_dataset)
      child.parent_attribute = node.attribute
      child.value = attr_value
      node.addChild(child)

    # Return the subtree/node
    return node
