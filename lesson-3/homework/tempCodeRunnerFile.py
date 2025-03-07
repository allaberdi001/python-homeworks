t=tuple(input("Enter elements with space in between: ").strip().split())
for i in range(len(t)):
    t[i]=int(t[i])
largest=t[0]
for i in range(len(t)):
    if t[i]>largest:
        largest=t[i]
print(largest)