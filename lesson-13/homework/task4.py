import numpy as np
import random
arr=np.array([random.randint(0,100) for i in range(27)])
arr=arr.reshape(3,3,3)
print(arr)
