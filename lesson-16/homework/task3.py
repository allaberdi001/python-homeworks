import numpy as np
import pandas as pd

df_iris=pd.read_json(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\iris.json")
print(df_iris.describe())
print(df_iris.median(numeric_only=True))

df_titanic=pd.read_excel(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\titanic.xlsx")
print(df_titanic["Age"].max())
print(df_titanic["Age"].min())
print(df_titanic["Age"].sum())
print()

df_movie=pd.read_csv(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\movie.csv")
print(df_movie.groupby("director_name")["director_facebook_likes"].sum().idxmax())
print(df_movie.sort_values(by="duration",ascending=False)[["movie_title","director_name"]].head(5))
