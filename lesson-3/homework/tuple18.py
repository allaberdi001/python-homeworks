a=tuple(input("Enter elements with space in between: ").strip().split())
t=tuple(map(int,a))

st=int(input("starting index of subtuple: "))
en=int(input("ending index of subtuple: "))
smallest=t[st]
for i in range(st+1,en+1):
    if smallest>t[i]:
        smallest=t[i]
print("smallest in the subtuple is: ",smallest)