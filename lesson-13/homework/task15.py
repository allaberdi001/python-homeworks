import numpy as np
import random
A=np.array([random.randint(0,100) for i in range(25)]).reshape(5,5)
print(A)
rows=np.array([A[i].sum() for i in range(5)])
columns=np.array([A[0:,i].sum() for i in range(5)])
for i in range(5):
    print("row ",i," sum: ",rows[i])
print()
for i in range(5):
    print("column ",i," sum: ",columns[i])