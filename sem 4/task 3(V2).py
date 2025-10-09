import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("iris_data.csv")
species=df['Species'].unique()
plt.pie([list(df["Species"]).count(i) for i in species], labels = species)
plt.title("доля разных видов (Species) ирисов в датасете")
plt.show()