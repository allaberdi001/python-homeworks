import numpy as np
import random
arr1=np.array([random.randint(0,100) for i in range(9)]).reshape(3,3)
det=np.linalg.det(arr1)
print(det)