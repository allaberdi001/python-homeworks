import random
import numpy as np
import matplotlib.pyplot as plt

x=np.random.randn(1000)
plt.hist(x,bins=30,alpha=0.8)
plt.title("normal distribution of 1000 values")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()