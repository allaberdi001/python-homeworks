import json
import csv
file=r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-9\homework\tasks.json"
def stats():
    count=len(tasks)
    completed=0
    avg_pri=0
    for task in tasks:
        avg_pri=avg_pri+int(task["priority"])
        if task["completed"]:
            completed=completed+1
    not_completed=count-completed
    avg_pri=round(avg_pri/count,2)
    print(f"""
Total tasks: {count},
Completed tasks: {completed},
Pending tasks: {not_completed},
Average priority: {avg_pri}

    """)

with open(file, "r") as f:
    tasks=json.load(f)
for task in tasks:
    print(f'{task["id"]}, {task["task"]}, {"completed" if task["completed"] else "not completed"}, {task["priority"]}')
stats()

file2=r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-9\homework\tasks.csv"

def convert():
    with open(file2,"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["ID","Task","Completed","Priority"])
        for task in tasks:
            l=[task["id"], task["task"], task["completed"], task["priority"]]
            writer.writerow(l)

convert()


