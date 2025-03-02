a=input("String: ").strip()
start=input("Starts with: ")
end=input("Ends with: ")
a=a.split()
if start==a[0]:
    print("Yes, starts with: ",start)
else:
    print("No, doesn't start with: ", start)
if end==a[-1]:
    print("Yes, ends with: ",end)
else:
    print("No, doesnt end with: ",end)