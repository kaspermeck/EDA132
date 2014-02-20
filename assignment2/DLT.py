from plurality_value import plurality_value as p_val
from Importance import importance as gain
import copy

def DLT(dataset, parent_dataset):
  if not dataset['data']:
    node = Node()
    node.value = p_val(parent_dataset)
    return node
  elif [x[-1] from x in dataset['data']][1:] == [x[-1] from x in dataset['data']][:-1]:
    node = Node()
    node.value = dataset['data'][0][-1]
    return node
  elif not dataset['attributes']:
    node = Node()
    node.value = p_val(dataset)
    return node
  else:
    # Find max gain
    gains = []
    for attr in dataset['attributes']:
      gains.append(gain(dataset, attr))

    max_attr_pos = gains.index(max(gains))

    # Create a new new for the tree
    node = Node()
    node.value = dataset['attributes'][max_attr_pos][0]

    # Clone the attributes list but remove the current attribute
    attributes_new = []
    for attr in dataset['attributes']:
      if attr != dataset['attributes'][max_attr_pos]:
        attributes_new.append(attr)

    # Branch the values
    for attr_value in dataset['attributes'][max_attr_pos][1]:
      data_new = []

      # Clone the data for the chosen attribute
      for data in dataset['data']:
        if data[max_attr_pos] == attr_value:
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

