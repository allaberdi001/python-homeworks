import numpy as np
@np.vectorize
def Fah_to_cel(f):
    c=int((f-32)*(5/9))
    return c
f=[32, 68, 100, 212, 77]
k=9
print(Fah_to_cel(f))
print(Fah_to_cel(k))