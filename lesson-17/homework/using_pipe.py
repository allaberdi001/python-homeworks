import pandas as pd

df_titanic = pd.read_excel(r"lesson-17\homework\titanic.xlsx")

titanic_result = (
    df_titanic
    .pipe(lambda df: df.loc[df["Survived"] == 1]) 
    .assign(
        Age=lambda df: df["Age"].fillna(df["Age"].mean()),  
        Fare_Per_Age=lambda df: df["Fare"] / df["Age"]     
    )
)

print(titanic_result.head())

df_flights = pd.read_parquet(r"lesson-17\homework\flights",["DepDelay"],engine="pyarrow")

flights_result = (
    df_flights
    .pipe(lambda df: df.loc[df["DepDelay"] > 30])  
    .assign(
        Delay_Per_Hour=lambda df: df["DepDelay"] / (df["sched_duration"] / 60)  
    )
)

print(flights_result.head())