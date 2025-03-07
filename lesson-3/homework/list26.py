l=input("Enter integers of a list with space in between: ").strip().split()
if len(l)%2==0:
    print(l[(len(l)-1)//2],l[(len(l)-1)//2+1])
else:
    print(l[(len(l)-1)//2])