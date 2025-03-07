l=input("Enter elements of a list with space in between: ").strip().split()
nl=[l[0]]
repeated=False
for i in range(len(l)):
    for j in range(len(nl)):
        if l[i]==nl[j]:
            repeated=True
    if repeated ==False:
        nl.append(l[i])
    repeated=False
print(nl)
