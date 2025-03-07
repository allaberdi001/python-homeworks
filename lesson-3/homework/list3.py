l=input("Enter numbers of a list with space in between: ").split(" ")
greatest=int(l[0])
for i in l:
    if int(i)>greatest:
        greatest=int(i)
print("greatest is: ", greatest)
