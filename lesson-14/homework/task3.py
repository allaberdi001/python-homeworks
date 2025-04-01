import numpy as np

A=[[4,5,6],
   [3,-1,1],
   [2,1,-2]]
b=[7,4,5]
sol=np.linalg.solve(A,b)
print(sol)