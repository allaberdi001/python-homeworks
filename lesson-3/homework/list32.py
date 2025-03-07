l1=input("Enter integers of a list with space in between: ").strip().split()
for i in range(len(l1)):
    l1[i]=int(l1[i])
l2=input("Enter integers of a list with space in between: ").strip().split()
for i in range(len(l2)):
    l2[i]=int(l2[i])
nl=l1+l2
nl.sort()
print(nl)