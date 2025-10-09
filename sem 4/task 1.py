import matplotlib.pyplot as plt
import numpy as np
x = [205, 245, 295, 335, 375, 415, 455, 505, 545, 615]
y = [1.4235, 1.421, 1.4225, 1.43, 1.4405, 1.454, 1.47, 1.494, 1.5155, 1.5555]
plt.figure(figsize=(10,6),dpi=100)
plt.scatter(x,y,color="r")
mnk=np.polyfit(x,y,2)
z = np.poly1d(mnk)
plt.plot(x,[z(i) for i in x],"b")
plt.errorbar(x, y, yerr=0.005, xerr = 10, color = 'k', linestyle = 'None')
plt.title("graphic")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()