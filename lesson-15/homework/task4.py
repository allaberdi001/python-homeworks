import matplotlib.pyplot as plt
import numpy as np
import random

x=np.array([random.uniform(0,10) for i in range(100)])
y=np.array([random.uniform(0,10) for i in range(100)])
colors=np.random.rand(100)

plt.scatter(x,y,c=colors,cmap="viridis",s=100)
plt.xlabel("X")
plt.ylabel("Y", rotation=0)
plt.title("Random X and Y")
plt.grid()
plt.show()