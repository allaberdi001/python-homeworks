import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2*np.pi,10000)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,c="r",linestyle="--",label=r"$sin(x)$")
plt.plot(x,y2,c="b",linestyle="-.",label=r"$cos(x)$")
plt.legend()
plt.show()