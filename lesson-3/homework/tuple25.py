t=tuple(input("Enter elements of a list with space in between: ").strip().split())
l=list(t)
nl=[l[0]]
repeated=False
for i in range(len(l)):
    for j in range(len(nl)):
        if l[i]==nl[j]:
            repeated=True
    if repeated ==False:
        nl.append(l[i])
    repeated=False
t_new=tuple(nl)
print(t_new)