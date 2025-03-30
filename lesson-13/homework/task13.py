import numpy as np
import random
arr1=np.array([random.randint(0,100) for i in range(9)]).reshape(3,3)
print(arr1)
arr2=np.array([random.randint(0,100) for i in range(3)])
print(arr2)
arr3=np.dot(arr1,arr2)
print(arr3)
print(arr2.reshape(3,1))
arr3=np.dot(arr1,arr2.reshape(3,1))
print(arr3)