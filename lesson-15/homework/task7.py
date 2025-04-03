import numpy as np
import matplotlib.pyplot as plt

products=['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values=[200, 150, 250, 175, 225]
colours=["b","g","y","k","r"]

plt.bar(products,values,color=colours)
plt.xlabel("Product names")
plt.ylabel("Sales values")
plt.title("Sales data")

plt.show()