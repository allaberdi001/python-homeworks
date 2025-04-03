import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,10000)
tl=x**3
tr=np.sin(x)
bl=np.e**x
br=np.log(x+1)
plt.figure(figsize=(8,6))

plt.subplot(2,2,1)
plt.plot(x,tl,c="r")
plt.title("x cubed")
plt.xlabel("X")
plt.ylabel("Y",rotation=0)

plt.subplot(2,2,2)
plt.plot(x,tr,c="b")
plt.title("sin(x)")
plt.xlabel("X")
plt.ylabel("Y",rotation=0)

plt.subplot(2,2,3)
plt.plot(x,bl,c="k")
plt.title("exponential function")
plt.xlabel("X")
plt.ylabel("Y",rotation=0)

plt.subplot(2,2,4)
plt.plot(x,br,c="g")
plt.title("logarithmic function")
plt.xlabel("X")
plt.ylabel("Y",rotation=0)

plt.tight_layout()
plt.show()