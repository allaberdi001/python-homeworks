l1=input("Enter elements of a list with space in between: ").strip().split()
l2=input("Enter elements of the sublist list with space in between: ").strip().split()
for i in range(len(l1)-len(l2)+1):
    if l1[i:i+len(l2)]==l2:
        print("Exist")
        break
    else:
        if i==len(l1)-len(l2):
            print("doesn't exist")