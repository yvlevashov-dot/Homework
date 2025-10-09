import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("iris_data.csv")
fig = plt.figure(figsize=(10,8))
ax1=fig.add_subplot(231)
ax2=fig.add_subplot(232)
ax3=fig.add_subplot(233)
ax4=fig.add_subplot(234)
ax5=fig.add_subplot(235)
ax6=fig.add_subplot(236)
ax1.scatter(df["SepalLengthCm"], df["SepalWidthCm"])
ax2.scatter( df["SepalLengthCm"],df["PetalLengthCm"])
ax3.scatter( df["SepalLengthCm"],df["PetalWidthCm"])
ax4.scatter( df["SepalWidthCm"],df["PetalLengthCm"])
ax5.scatter( df["SepalWidthCm"],df["PetalWidthCm"])
ax6.scatter( df["PetalLengthCm"],df["PetalWidthCm"])
plt.show()