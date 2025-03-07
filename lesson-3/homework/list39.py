l=input("Enter elements of a list with space in between: ").strip().split()
size=int(input("size: "))
l=[l[i:i+size] for i in range(0,len(l),size)]

print(l)