class Node(object):
  def __init__(self):
    self.children = []
    self.value = ""

  def addChild(self, node):
    self.children.append(node)
    
  def removeChild(self, node):
    if node in self.childen:
      self.children.remove(node) 

  def isLeaf(self):
    if not self.children:
      return True
    else:
      return False
