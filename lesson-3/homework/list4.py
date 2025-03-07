l=input("Enter numbers of a list with space in between: ").split(" ")
smallest=int(l[0])
for i in l:
    if int(i)<smallest:
        smallest=int(i)
print("smallest is: ", smallest)
