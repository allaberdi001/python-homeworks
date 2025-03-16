file=r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-7\homework\employees.txt"

class Employee:
    def __init__(self,employee_id,name,position,salary):
        self.employee_id=employee_id
        self.name=name
        self.position=position
        self.salary=salary
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self):
        self.menu()
    def menu(self):
        while True:
            print("""1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")
            try:
                choice=int(input("Enter your choice: "))
                if choice==1:
                    self.add_employee()
                elif choice==2:
                    self.view_all()
                elif choice==3:
                    self.search_for_employee()
                elif choice==4:
                    self.update_info()
                elif choice==5:
                    self.delete_record()
                elif choice==6:
                    print("Goodbye!")
                    break
                else:
                    print("Enter in the range(1-6) ")
            except ValueError:
                print("Enter integer value, not other type")  
    def add_employee(self):
        employee_id=input("Employee ID: ")
        name=input("Employee name: ")
        position=input("Position: ")
        while True:
            try:
                salary=int(input("Salary (just integer) "))
                break
            except:
                print("Enter integer for salary!!")

        if self.validation(employee_id):
            new_employee=Employee(employee_id,name,position,salary)
            with open(file,"a") as f:
                f.write(str(new_employee)+"\n")
            print("New employee added")
        else:
            print("Employee with this ID already exists")
    def validation(self,employee_id):
        with open(file,"r") as f:
            lines=f.readlines()
            for line in lines:
                if line.split(", ")[0]==employee_id:
                    return False
            return True
    def view_all(self):
        with open(file,"r") as f:
            all=f.read()
            print(all)
    def search_for_employee(self,employee_id):
        employee_id=str(employee_id)
        with open(file,"r") as f:
            found=False
            lines=f.readlines()
            for line in lines:
                if line.split(", ")[0]==employee_id:
                    print(line)
                    found=True
        if not found:
            print("No such employee exist!")
    def update_info(self):
        employee_id=input("Which employee you want to update (eneter id): ")
        while self.validation(employee_id):
            employee_id=input("This employee doesn't exist!! Which employee you want to update? (eneter id): ")
        new_employee_id=input("Updated Employee ID: ")
        name=input("Updated Employee name: ")
        position=input("Updated Position: ")
        while True:
            try:
                salary=int(input("Salary (just integer): "))
                break
            except:
                print("Enter integer for salary!!")
        if not self.validation(new_employee_id):
            print("There is already an employee with the same ID!!")
        else:
            l=[]
            with open(file,"r") as f:
                lines=f.readlines()
            with open(file,"w") as f:
                for line in lines:
                    if line.split(", ")[0]!=employee_id:
                        l.append(line)
                    else:
                        l.append(f"{new_employee_id}, {name}, {position}, {salary}\n")
                for line in l:
                    f.write(line)
    def delete_record(self):
        employee_id=input("Which employee you want to delete (eneter id): ")
        while self.validation(employee_id):
            employee_id=input("This employee doesn't exist!! Which employee you want to delete? (eneter id): ")
        l=[]
        with open(file,"r") as f:
            lines=f.readlines()
        with open(file,"w") as f:
            for line in lines:
                if line.split(", ")[0]!=employee_id:
                    l.append(line)
            for line in l:
                f.write(line)
        print("deleted")
        
            
    

        
    

managing=EmployeeManager()
