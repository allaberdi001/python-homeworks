import numpy as np
import pandas as pd
import sqlite3

df_iris=pd.read_json(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\iris.json")
df_iris.columns=df_iris.columns.str.lower()
print(df_iris[['sepallength', 'sepalwidth']])
print()

df_titanic=pd.read_excel(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\titanic.xlsx")
print(df_titanic[df_titanic["Age"]>30])
print(df_titanic["Sex"].value_counts())
print()

df_flights=pd.read_parquet(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\flights",columns=["Origin","Dest","CarrierDelay"])
print(df_flights)
print("num of unique destinations:", df_flights["Dest"].nunique())
print()

df_movie=pd.read_csv(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\movie.csv")
df_filtered=df_movie[df_movie["duration"]>120]
print(df_filtered)
df_filtered=df_filtered.sort_values(by="director_facebook_likes",ascending=False)
print(df_filtered)