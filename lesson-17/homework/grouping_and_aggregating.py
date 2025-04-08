import pandas as pd

df_titanic=pd.read_excel(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-17\homework\titanic.xlsx")
df_pclass=df_titanic.groupby("Pclass").agg(
    {
        "Age":"mean",
        "Fare":"sum",
        "PassengerId":"count"
    }
)
print(type(df_pclass))

df_movie=pd.read_csv(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-17\homework\movie.csv")
df_groups=df_movie.groupby(["color","director_name"]).agg({
    "num_critic_for_reviews":"sum",
    "duration":"mean"
})
print(df_groups)

df_flights=pd.read_parquet(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-17\homework\flights",columns=["Flights","Year","Month","ArrDelay","DepDelay"])
new_df=df_flights.groupby(["Year","Month"]).agg(
    TotalFlights=("Flights","sum"),
    AverageArrDelay=("ArrDelay","mean"),
    MaxDepDelay=("DepDelay","max")
)
print(new_df)