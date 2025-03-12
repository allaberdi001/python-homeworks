
option=int(input("""1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit.
Enter your choice: """))
if option==1:
    with open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-6\homework\employees.txt","a") as f:
        employee_id=input("employee id: ")
        name=input("name: ")
        position=input("position: ")
        salary=input("salary: ")
        line=f"{employee_id},{name},{position},{salary}\n"
        f.write(line)
elif option==2:
    with open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-6\homework\employees.txt","r") as f:
        print(f.read())
elif option==3:
    employee_id=input("employee id: ")
    found=False
    with open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-6\homework\employees.txt","r") as f:
        lines=f.readlines()
        for line in lines:
            if line[:line.index(",")]==employee_id:
                print (line)
                found=True
                break
    if not found:
        print("Employee with that id is not found")
elif option==4:
    employee_id=input("employee id: ")
    found=False
    lines=[]
    with open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-6\homework\employees.txt","r") as f:
        lines=f.readlines()
        for line in lines:
            if line[:line.index(",")]==employee_id:
                found=True
                print (f"Current state: {line}\n Enter updated into ")
                employee_id=input("employee id: ")
                name=input("name: ")
                position=input("position: ")
                salary=input("salary: ")
                lines[lines.index(line)]=f"{employee_id},{name},{position},{salary}\n"
                break
    if not found:
        print("Such employee is not found")
    else:
        with open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-6\homework\employees.txt","w") as f:
            f.write("".join(lines))
            print("updated")
elif option==5:
    employee_id=input("employee id: ")
    found=False
    lines=[]
    with open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-6\homework\employees.txt","r") as f:
        lines=f.readlines()
        for line in lines:
            if line[:line.index(",")]==employee_id:
                found=True
                print (f"Current state: {line}")
                lines.remove(line)
                break
    if not found:
        print("Such employee is not found")
    else:
        with open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-6\homework\employees.txt","w") as f:
            f.write("".join(lines))
            print("deleted")
elif option==6:
    pass
else:
    print("not specified option")