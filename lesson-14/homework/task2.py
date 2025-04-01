import numpy as np
np.vectorize
def power(num,pow):
    return np.array(num)**np.array(pow)

num=[2, 3, 4, 5]
pow=[1, 2, 3, 4]
print(power(num,pow))
print(power(2,3))