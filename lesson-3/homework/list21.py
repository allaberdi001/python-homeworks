l=input("Enter elements of a list with space in between: ").strip().split()
for i in range(len(l)):
    l[i]=int(l[i])
l.sort()
print(l[1])