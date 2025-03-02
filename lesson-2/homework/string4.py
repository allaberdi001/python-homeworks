a=input("Kiriting: ")
if len(a)%2==1:
    if a[0:len(a)//2]==a[-1:len(a)//2:-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
else:
    if a[0:len(a)//2]==a[-1:len(a)//2-1:-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

