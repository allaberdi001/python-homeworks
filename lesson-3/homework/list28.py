l=input("Enter integers of a list with space in between: ").strip().split()
for i in range(len(l)):
    l[i]=int(l[i])
st=int(input("starting index of sublist: "))
en=int(input("ending index of sublist: "))
smallest=l[st]
for i in range(st+1,en+1):
    if smallest>l[i]:
        smallest=l[i]
print("smallest in the subset is: ",smallest)