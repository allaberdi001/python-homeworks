l=input("Enter integers of a list with space in between: ").strip().split()
total=0
for i in range(len(l)):
    l[i]=int(l[i])
    if l[i]<0:
        total=total+l[i]

print(total)