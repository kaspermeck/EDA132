from readARFF import readARFF
from DLT import DLT



if __name__ == "__main__":
  dataset = readARFF("vote.arff")
  tree = DLT(dataset,dataset)
  tree.printt()
  
