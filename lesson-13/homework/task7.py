import numpy as np
import random
arr=np.array([random.randint(0,100) for i in range(25)]).reshape(5,5)
print(arr)
arr=(arr-arr.mean())/arr.std()
print(arr)

