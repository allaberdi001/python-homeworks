s=set(input("Enter elements with space in between: ").strip().split())
l=list(s)
l.sort()
print(l[-1])