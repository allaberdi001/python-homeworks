import random
st=int(input("start: "))
en=int(input("end: "))
size=int(input("what size: "))
s=set(random.sample(range(st,en+1),size))
print(s)