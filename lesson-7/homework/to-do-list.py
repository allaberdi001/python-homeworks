import re
import csv
import json

file=r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-7\homework\to-do.json"
tasks=[]

def get_valid_date():
    pattern=r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    while True:
        date_str=input("Enter date (YYYY-MM-DD): ")

        if not re.fullmatch(pattern, date_str):
            print("Invalid format! Please enter in YYYY-MM-DD format.")
            continue
        else:
            return date_str
def get_status():
    while True:
        status=input("Enter status(In Progress, Completed): ")
        if status not in ["In Progress","Completed"]:
            print("Wrong status entered!")
            continue
        else:
            return status

def add_new_task():
    id=input("Enter task ID: ")
    if not unique(id):
        id=input("This id already exist. Enter different task ID: ")
    title=input("Enter task title: ")
    description=input("Enter task Description: ")
    due_date=get_valid_date()
    status=get_status()
    task=f"{id}, {title}, {description}, {due_date}, {status}\n"
    tasks.append(task)
def unique(id):
    for task in tasks:
        if task.split(", ")[0]==id:
            return False
    return True
def view_all():
    extention=file[file.index(".")+1:len(file)]
    if extention=="txt":
        with open(file,"r") as f:
            all=f.read()
            print(all)
    elif extention=="csv":
        with open(file,"r") as f:
            reader=csv.reader(f)
            for row in reader:
                print(", ".join(row))
    elif extention=="json":
        with open(file,"r") as f:
            try:
                data=json.load(f)
                for row in data["tasks"]:
                    print(f'{row["id"]}, {row["title"]}, {row["description"]}, {row["due-date"]}, {row["status"]}\n')
            except:
                print("There are no tasks")

def update_task():
    while True:
        id=input("Which task to update? Enter ID: ")
        if unique(id):
            print("Task with this id doesn't exist!!!")
            continue
        else:
            break
    new_id=input("Enter updated task ID: ")
    if not unique(new_id):
        new_id=input("This id already exist. Enter different task ID: ")
    title=input("Enter updated task title: ")
    description=input("Enter updated task Description: ")
    due_date=get_valid_date()
    status=get_status()
    task=f"{new_id}, {title}, {description}, {due_date}, {status}\n"
    for line in tasks:
        if line.split(", ")[0]==id:
            tasks[tasks.index(line)]=task
        
def delete_task():
    while True:
        id=input("Which task to delete? Enter ID: ")
        if unique(id):
            print("Task with this id doesn't exist!!!")
            continue
        else:
            break
    
    for line in tasks:
        if line.split(", ")[0]==id:
            tasks.remove(line)
    print("task deleted")
def filter_task():
    print("Filter by (In Progress/Completed): ")
    status=get_status()
    l=[]
    for task in tasks:
        if task.strip().split(", ")[4]==status:
            l.append(task)
    print("All tasks that are ",status)
    for i in l:
        print(i.strip())
    print("*******")
def save_tasks():
    extention=file[file.index(".")+1:len(file)]
    if extention=="txt":
        with open(file,"w") as f:
            for task in tasks:
                f.write(task)
    elif extention=="csv":
        data=[]
        for task in tasks:
            row=task.strip().split(", ")
            data.append(row)
        with open(file,"w",newline="") as f:
            writer=csv.writer(f)
            writer.writerows(data)
    elif extention=="json":
        data={}
        data["tasks"]=[]
        for task in tasks:
            task=task.strip().split(", ")
            dict={}
            dict["id"]=task[0]
            dict["title"]=task[1]
            dict["description"]=task[2]
            dict["due-date"]=task[3]
            dict["status"]=task[4]
            data["tasks"].append(dict)
            with open(file,"w") as f:
                json.dump(data,f,indent=4)



def load_tasks():
    global tasks
    tasks=[]
    extention=file[file.index(".")+1:len(file)]
    print(extention)
    if extention=="txt":
        with open(file, "r") as f:
            tasks=f.readlines()
    elif extention=="csv":
        with open(file,"r") as f:
            reader=csv.reader(f)
            for row in reader:
                tasks.append(", ".join(row)+"\n")
    elif extention=="json":
        with open(file,"r") as f:
            try:
                data=json.load(f)
            except:
                data={}
        if data!={}:
            for row in data["tasks"]:
                task=row["id"]+row["title"]+row["description"]+row["due-date"]+row["status"]+"\n"
                tasks.append(task)
            




load_tasks()
while True:
    choice=input("""Welcome to the To-Do Application!
    1. Add a new task
    2. View all tasks
    3. Update a task
    4. Delete a task
    5. Filter tasks by status
    6. Save tasks
    7. Load tasks
    8. Exit

    Enter your choice:""")
    if choice=='1':
        add_new_task()
    elif choice=='2':
        view_all()
    elif choice=='3':
        update_task()
    elif choice=='4':
        delete_task()
    elif choice=='5':
        filter_task()
    elif choice=='6':
        save_tasks()
    elif choice=='7':
        load_tasks()
    elif choice=='8':
        print("Goodbye!")
        break
    else:
        print("Enter in range (1-8)!")
