import numpy as np
import pandas as pd
import sqlite3

conn=sqlite3.connect(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\chinook.db")
df=pd.read_sql_query("select * from customers",conn)
print("database")
print(df.head(10))

df_json=pd.read_json(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\iris.json")
print("json")
print(df_json.shape)
print(df_json.columns)
print()

df_excel=pd.read_excel(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\titanic.xlsx")
print("excel")
print(df_excel.head(5))
print()

import pyarrow.parquet as pq

# Point to the dataset (folder or file)
parquet_file = pq.ParquetDataset(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\flights")

# Get the schema (column names and types)
print(parquet_file.schema)

df_flights=pd.read_parquet(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\flights",columns=["Year","Quarter","Month"])
print("parquet")
df_flights.info()
print()

df_csv=pd.read_csv(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-16\homework\movie.csv")
print("csv")
print(df_csv.head(10))
print()
print("random 10 movies")

print(df_csv.sample(10))
