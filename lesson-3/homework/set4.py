s1=set(input("Enter elements with space in between: ").strip().split())
s2=set(input("subset: Enter elements with space in between: ").strip().split())
s3=s1&s2
if s3==s2:
    print("yes, subset")
else:
    print("no, not subset")