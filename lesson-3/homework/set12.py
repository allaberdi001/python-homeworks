s=set(input("Enter elements with space in between: ").strip().split())
elm=input("element ")
if elm not in s:
    s.add(elm)
    print("added ",s)
else:
    print("not added, ",s)