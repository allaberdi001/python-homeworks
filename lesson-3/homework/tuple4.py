t=tuple(input("Enter elements with space in between: ").strip().split())
elm=input("enter element: ")
if elm in t:
    print(True)
else:
    print(False)