import matplotlib.pyplot as plt
import numpy as np
import re
import pandas as pd
from matplotlib.ticker import (AutoMinorLocator,
                               MultipleLocator)
def transform_date(str):
    dateRegex = re.compile(r'(\d\d\d\d)-(\d\d)-(\d\d)')
    new_date = dateRegex.search(str)
    return('{}-{}-{}'.format(new_date.group(3), new_date.group(2), new_date.group(1)))
df = pd.read_csv("BTC_data.csv")
dt1 = df["time"]
dt = []
fig, ax = plt.subplots(figsize = (12, 8))
ax.grid()
for i in dt1:
    dt.append(transform_date(i))
price = df["close"]
plt.xticks(rotation = 75)
plt.plot(dt,price)

dt2=[]
for i in range(len(price)):
    dt2.append(i)
z = np.polyfit(dt2, price, 50)
p = np.poly1d(z)
ax.xaxis.set_major_locator(plt.AutoLocator())
plt.plot(dt2,[p(i) for i in dt2],"r")
plt.show()