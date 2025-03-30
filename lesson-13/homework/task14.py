import numpy as np
import random
A=np.array([random.randint(0,100) for i in range(9)]).reshape(3,3)
print(A)
b=np.array([random.randint(0,100) for i in range(3)])
print(b)
det=np.linalg.det(A)
if np.isclose(det,0):
    x=np.linalg.lstsq(A,b,rcond=None)[0]
    print("Either infinitely many solutions or no solutions")
else:
    x=np.linalg.solve(A, b)
    
    print("Unique solution")
    print(x)

