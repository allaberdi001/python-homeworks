t=tuple(input("Enter elements of a tuple with space in between: ").strip().split())
l=list(t)
pal=True
for i in range((len(l)-1)//2):
    if l[i]!=l[-i-1]:
        pal=False
print(pal)

