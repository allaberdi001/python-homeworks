a=tuple(input("Enter elements with space in between: ").strip().split())
t=tuple(map(int,a))
t_new=tuple(sorted(t))
if t==t_new:
    print(True)
else:
    print(False)
