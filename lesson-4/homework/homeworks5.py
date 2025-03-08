password=input("password: ")
if len(password)<8:
    print("Password is too short.")
else:
    if password.lower()==password:
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong")