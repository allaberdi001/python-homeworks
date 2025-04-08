import sqlite3
import pandas as pd

conn=sqlite3.connect(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-17\homework\chinook.db")
cursor=conn.cursor()
df_customers=pd.read_sql("select * from customers", con=conn)
df_invoices=pd.read_sql("select * from invoices", con=conn)
customers_invoices=pd.merge(df_customers,df_invoices,on="CustomerId")
print(customers_invoices.groupby("CustomerId").size())

df_movie=pd.read_csv(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-17\homework\movie.csv")
df_color=df_movie[["director_name","color"]]
df_critic=df_movie[["director_name","num_critic_for_reviews"]]
print(df_color)
left_join=pd.merge(df_color,df_critic,on="director_name",how="left")
outer_join=pd.merge(df_color,df_critic,on="director_name",how="outer")

print(left_join)
print(outer_join)
print(left_join.shape[0])
print(outer_join.shape[0])
