a=input("String: ")

vowels='aeuioAEUIO'
for char in vowels:
    a=a.replace(char, "*")
print(a)