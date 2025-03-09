a=int(input("Enter a positive integer: "))
for i in range(1,a+1):
    if a%i==0:
        print(f"{i} is a factor of {a}")
