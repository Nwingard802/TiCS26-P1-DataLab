import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("SeigeData.csv")
map = data["Map"]
rank = data["Rank"]
KD = data["KDRatio"]

graph = plt.scatter(map, KD, c="darkred")

plt.show()