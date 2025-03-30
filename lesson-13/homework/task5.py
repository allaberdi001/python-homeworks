import numpy as np
import random
arr=np.array([random.randint(0,100) for i in range(100)])
arr=arr.reshape(10,10)
print(arr)
print("max: ",arr.max())
print("min: ",arr.min())
