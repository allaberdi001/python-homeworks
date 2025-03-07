l=input("Enter integers of a list with space in between: ").strip().split()
for i in range(len(l)):
    l[i]=int(l[i])
st=int(input("starting index of sublist: "))
en=int(input("ending index of sublist: "))
largest=l[st]
for i in range(st+1,en+1):
    if largest<l[i]:
        largest=l[i]
print("largest in the sublist is: ",largest)