l=input("Enter elements of a list with space in between: ").strip().split()
pal=True
for i in range((len(l)-1)//2):
    if l[i]!=l[-i-1]:
        pal=False
print(pal)

