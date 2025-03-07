a=tuple(input("Enter elements with space in between: ").strip().split())
t=tuple(map(int,a))
largest=t[0]
for i in range(len(t)):
    if t[i]>largest:
        largest=t[i]
print(largest)
