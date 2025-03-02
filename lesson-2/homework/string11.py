a=input("kiriting: ")
if any(char.isdigit() for char in a):
    print("Digit(s) are present")
else:
    print("Digits are not present")