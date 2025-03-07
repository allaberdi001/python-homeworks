s=set(input("Enter elements with space in between: ").strip().split())
elm=input("element ")
if elm in s:
    print("exist")
else:
    print("not exist")