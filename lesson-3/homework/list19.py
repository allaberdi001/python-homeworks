l=input("Enter elements of a list with space in between: ").strip().split()
elm=input("Which element to change: ")
new=input("what to replace with: ")
i=0
replaced=False
while replaced==False and i<=len(l):
    if l[i]==elm:
        l[i]=new
        replaced=True
    else:
        i=i+1
print(l)