a=tuple(input("Enter elements with space in between: ").strip().split())
t=tuple(map(int,a))
smallest=t[0]
for i in range(len(t)):
    if t[i]<smallest:
        smallest=t[i]
print(smallest)
