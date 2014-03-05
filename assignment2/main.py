from readARFF import readARFF
from Importance import compute_split_points_for_reals
from DLT import DLT



if __name__ == "__main__":
  # read data
  dataset = readARFF("weather.arff")
  #dataset = readARFF("weather.nominal.arff")

  # prepare dataset (convert ints)
  dataset = compute_split_points_for_reals(dataset)

  # compute the tree and print it
  tree = DLT(dataset,dataset)
  tree.printt()
