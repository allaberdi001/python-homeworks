s=set(input("Enter elements with space in between: ").strip().split())
s=map(int,s)
l=list(s)
s_new=set()
for i in range(len(l)):
    if l[i]%2==1:
        s_new.add(l[i])
print(s_new)