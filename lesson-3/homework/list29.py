l=input("Enter elements of a list with space in between: ").strip().split()
i=int(input("enter index: "))
if i<=len(l)-1:
    l.remove(l[i])
print(l)