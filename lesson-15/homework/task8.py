import numpy as np
import matplotlib.pyplot as plt

categories=['Category A', 'Category B', 'Category C']
periods=['T1', 'T2', 'T3', 'T4']
A=np.array([3,4,2,7])
B=np.array([1,2,3,4])
C=np.array([6,5,3,3])

x=np.arange(len(periods))
plt.bar(x,A,label=categories[0],color="b")

plt.bar(x,B,bottom=A,label=categories[1],color="g")
plt.bar(x,C,bottom=A+B,label=categories[2],color="y")

plt.xlabel("periods")
plt.ylabel("contributions")
plt.title("Stacked Bar Chart")
plt.xticks(x, periods) 
plt.legend()

plt.show()
