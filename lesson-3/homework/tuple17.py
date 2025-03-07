a=tuple(input("Enter elements with space in between: ").strip().split())
t=tuple(map(int,a))

st=int(input("starting index of subtuple: "))
en=int(input("ending index of subtuple: "))
largest=t[st]
for i in range(st+1,en+1):
    if largest<t[i]:
        largest=t[i]
print("largest in the subtuple is: ",largest)