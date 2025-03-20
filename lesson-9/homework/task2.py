import csv
file=r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-9\homework\grades.csv"
with open(file,"r") as f:
    reader=csv.DictReader(f)
    subjects=[]
    for row in reader:
        subjects.append(row["Subject"])
    count=len(subjects)
    subjects=list(set(subjects))
    subject_count={}
    for subject in subjects:
        subject_count[subject]=0
    points=[0 for i in range(len(subjects))]
    subjects_dict=dict(zip(subjects,points))
    subjects_count={}
    for subject in subjects:
        f.seek(0)
        for row in reader:
            if row['Subject']==subject:
                subject_count[subject]=subject_count[subject]+1
                subjects_dict[subject]=subjects_dict[subject]+int(row['Grade'])
for key, value in subjects_dict.items():
    subjects_dict[key]=round(value/subject_count[key], 1)
subjects_dict={"Subject":"Average Grade", **subjects_dict}
print(subjects_dict)
new=[[k,v] for k,v in subjects_dict.items()]

print(new)
file2=r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-9\homework\average_grades.csv"
with open(file2,"w",newline="") as f:
    writer=csv.writer(f)
    writer.writerows(new)
