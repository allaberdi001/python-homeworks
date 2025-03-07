l=input("Enter elements of a list with space in between: ").strip().split(" ")
if len(l)==1 and l[0]=="":
    print("Empty list")
else:
    print(l[0])
