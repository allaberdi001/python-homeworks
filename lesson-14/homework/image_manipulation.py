import numpy as np
from PIL import Image
import random

img=Image.open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-14\homework\birds.jpg")
arr=np.array(img)
arr1=arr[:,::-1]
img1=Image.fromarray(arr1)
Image._show(img1)
arr2=arr[::-1,:]
img2=Image.fromarray(arr2)
Image._show(img2)
noice=np.array([random.randint(0,100) for i in range(720*720*3)],dtype=np.uint8).reshape(720,720,3)
arr3=arr+noice
img3=Image.fromarray(arr3)
Image._show(img3)
inc=np.array([200 for i in range(720*720)],dtype=np.uint8).reshape(720,720)
arr4=arr.copy()
print("ARR",arr4)
arr4[:,:,0]=arr4[:,:,0]+inc
arr4[arr4>255]=255
print("ARR",arr4)
img4=Image.fromarray(arr4)
Image._show(img4)
arr5=arr.copy()
arr5[100:200,100:200,:]=0
img5=Image.fromarray(arr5)
Image._show(img5)
