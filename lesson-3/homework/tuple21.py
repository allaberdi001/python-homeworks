t=tuple(input("Enter elements with space in between: ").strip().split())
num=int(input("what is number: "))
s=set(t)
t=tuple(s)
t=t*num
print(t)