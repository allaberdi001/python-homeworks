t=tuple(input("Enter elements with space in between: ").strip().split())
size=int(input("what is size: "))
l=list(t)
l=[l[i:i+size] for i in range(0,len(l),size)]
t=tuple(l)
print(t)