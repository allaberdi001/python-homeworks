import numpy as np
import random
arr1=np.array([random.randint(0,100) for i in range(15)]).reshape(5,3)
print(arr1)
arr2=np.array([random.randint(0,100) for i in range(6)]).reshape(3,2)
print(arr2)
arr4=np.dot(arr1,arr2)
print(arr4)