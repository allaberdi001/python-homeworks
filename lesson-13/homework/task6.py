import numpy as np
import random
arr=np.array([random.randint(0,100) for i in range(30)])

print(arr.sum()/len(arr))