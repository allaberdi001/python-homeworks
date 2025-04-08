import pandas as pd

def classify_age(age):
    if pd.isna(age):
        return "Unknown"
    elif age<18:
        return "Child"
    else:
        return "Adult"

df_titanic=pd.read_excel(r"lesson-17\homework\titanic.xlsx")
df_titanic["Age_group"]=df_titanic["Age"].apply(classify_age)

print(df_titanic)

df_employee=pd.read_csv(r"lesson-17\homework\employee.csv")
df_employee["Normalized_Salary"] = df_employee.groupby("DEPARTMENT")["BASE_SALARY"].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)

# 3. Check result
print(df_employee[["UNIQUE_ID","DEPARTMENT", "BASE_SALARY", "Normalized_Salary"]])

def classify_duration(duration):
    if pd.isna(duration):
        return "Unknown"
    elif duration<60:
        return "Short"
    elif duration<120:
        return "Medium"
    else:
        return "Long"
    
df_movie=pd.read_csv(r"lesson-17\homework\movie.csv")
df_movie["duration_class"]=df_movie["duration"].apply(classify_duration)
print(df_movie)