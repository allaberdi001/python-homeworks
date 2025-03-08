print(2)
for i in range(3,101):
    prime=True
    for j in range(2,i//2+1):
        if i%j==0:
            prime=False
            break
    if prime:
        print(i)
        
