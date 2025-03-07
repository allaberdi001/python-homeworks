a=tuple(input("Enter elements with space in between: ").strip().split())
t=tuple(map(int,a))
new_t=sorted(t)
print(new_t[1])