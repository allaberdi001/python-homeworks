l=input("Enter integers of a list with space in between: ").strip().split()
count=0
for i in range(len(l)):
    l[i]=int(l[i])
    if l[i]%2==1:
        count=count+1
print(count)
    