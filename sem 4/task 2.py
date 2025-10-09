import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,8))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
values1 = np.random.normal(0,50,1000)
values2 = np.random.normal(0,50,10000)
ax1.hist(values1,100)
ax2.hist(values2,100)
ax1.set_title('Hist of values')
ax2.set_title('hist of values2')
plt.show()