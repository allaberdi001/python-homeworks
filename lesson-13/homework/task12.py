import numpy as np
import random
arr1=np.array([random.randint(0,100) for i in range(12)]).reshape(3,4)
print(arr1)
arr2=np.array([random.randint(0,100) for i in range(12)]).reshape(4,3)
print(arr2)
arr3=np.dot(arr1,arr2)
print(arr3)