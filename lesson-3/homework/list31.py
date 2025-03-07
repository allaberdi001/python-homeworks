l=input("Enter elements of a list with space in between: ").strip().split()
n=int(input("how many times: "))

l=list(set(l))
l=l*n
print(l)