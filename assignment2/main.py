from readARFF import readARFF
from Importance import importance

if __name__ == "__main__":
  dataset = readARFF("weather.arff")
  gain1 = importance(dataset, "outlook")
  gain2 = importance(dataset, "windy")
  print gain1, gain2

