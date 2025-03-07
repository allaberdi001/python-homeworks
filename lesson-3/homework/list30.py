l=input("Enter integers of a list with space in between: ").strip().split()
for i in range(len(l)):
    l[i]=int(l[i])
ordered=True
for i in range(len(l)-1):
    if l[i+1]<l[i]:
        ordered=False
print(ordered)