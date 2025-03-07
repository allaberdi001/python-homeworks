l=input("Enter elements of a list with space in between: ").strip().split(" ")
nl=list(set(l.copy()))
print(nl)