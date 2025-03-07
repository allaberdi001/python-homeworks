l=input("Enter elements of a list with space in between: ").strip().split()
shift=int(input("how much to shift to right: "))
if shift>=len(l):
    shift=shift-len(l)
temp=[None for i in range(shift)]
for i in range(-1,(-shift)-1,-1):
    temp[i]=l[i]
count=-1
for i in range(len(l)-shift-1,-1,-1):
    l[count]=l[i]
    count=count-1
l=l[shift:len(l)]
l=temp+l
print(l)


