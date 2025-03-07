a=int(input("starting value: "))
b=int(input("ending value: "))
t=[]
for i in range(a,b+1):
    t.append(i)
t=tuple(t)
print(t)