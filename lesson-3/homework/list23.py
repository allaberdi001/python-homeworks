l=input("Enter integers of a list with space in between: ").strip().split()
nl=[]
for i in range(len(l)):
    l[i]=int(l[i])
    if l[i]%2==1:
        nl.append(l[i])
print(nl)