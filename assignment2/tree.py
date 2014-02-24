class Node(object):
  def __init__(self):
    self.children = []
    self.value = ""
    self.attribute = ""
    self.parent_attribute = ""

  def addChild(self, node):
    self.children.append(node)
    
  def removeChild(self, node):
    if node in self.childen:
      self.children.remove(node) 

  def isLeaf(self):
    return not self.children

  def printt(self):
    self.printRecursive(0, 4)

  def printRecursive(self, depth, indent):
    if depth == 0:
      for child in self.children:
        child.printRecursive(depth+1, indent)
    elif self.isLeaf():
      print ' ' * indent*(depth-1), self.parent_attribute, "=", self.value, "->", self.answer 
    else:
      print ' ' * indent*(depth-1), self.parent_attribute, "=", self.value
      for child in self.children:
        child.printRecursive(depth+1, indent)

