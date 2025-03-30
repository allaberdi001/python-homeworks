import numpy as np
import random
arr1=np.array([random.randint(0,100) for i in range(16)]).reshape(4,4)
print(arr1)
new_arr=arr1.T
print(new_arr)