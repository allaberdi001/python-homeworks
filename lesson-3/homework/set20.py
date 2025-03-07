s1=set(input("Enter integers of a list with space in between: ").strip().split())
s2=set(input("Enter integers of a list with space in between: ").strip().split())
if len(s1&s2)==0:
    print("nothing in common")
else:
    print("something in common")