from plurality_value import plurality_value as p_val
from Importance import importance as gain
import copy
from tree import Node as Node

def DLT(dataset, parent_dataset):

  if not dataset:
    if not parent_dataset:
      return ''
    else:
      node = Node()
      node.value = p_val(parent_dataset)
      return node

  # creates an array with all the last column data values
  data = dataset['data']
  dataLastCol = []
  for line in data:
    dataLastCol.append(line[-1])

  if all(x == dataLastCol[0] for x in dataLastCol):
    node = Node()
    # all values are the same in dataLastCol, choose any index
    node.value = dataLastCol[0]
    return node
  
  elif not dataset['attributes']:
    # if there are no attributes left in the dataset
    node = Node()
    node.value = p_val(dataset)
    return node
  
  else:
    # Find max gain
    gains = []
    attributes = dataset['attributes']
    for attr in attributes:
      gains.append(gain(dataset, attr))

    max_attr_index = gains.index(max(gains))
    max_attr = attributes[max_attr_index]
    # Create a new new for the tree
    node = Node()
    node.value = max_attr[0]

    # Clone the attributes list but remove the current attribute
    attributes_new = []
    for attr in attributes:
      if attr != max_attr:
        attributes_new.append(attr)

    # Branch the values
    for attr_value in max_attr:
      data_new = []

      # Clone the data for the chosen attribute
      for dataLine in data:
        if dataLine[max_attr_pos] == attr_value:
          d = list(data) # copy the tuple to a new list
          d.remove(max_attr_pos) # remove the current attribute
          data_new.append(tuple(d))

      # Create the branched dataset
      branched_dataset = []
      branched_dataset['attributes'] = attributes_new
      branched_dataset['data'] = data_new

      # Create the subtree/child
      child = DLT(branched_dataset, dataset) #DLT(dataset, parent_dataset)
      node.addChild(child)

    # Return the subtree/node
    return node