def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    prime=True
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            prime=False
            return False
    return prime
