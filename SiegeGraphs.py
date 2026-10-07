import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("SeigeData.csv")
map = data["Map"]
rank = data["Rank"]
KD = data["KDRatio"]

plt.figure(facecolor="#CCFFF6")
graph = plt.scatter(KD, map, c="darkred")
plt.xlabel("Maps")
plt.ylabel("K/D Ratio")
ax = plt.gca()
ax.set_facecolor("#B9E2DCBA")

plt.show()