
import sqlite3
conn=sqlite3.connect(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-11\homework\roster.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE Roster(
    Name TEXT,
    Species TEXT,
    Age INTEGER
    );
""")
data=[
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]
cursor.executemany("INSERT INTO Roster (Name,Species,Age) VALUES(?,?,?)",data)
cursor.execute("UPDATE Roster SET Name = ? where name=?",("Ezri Dax","Jadzia Dax"))

cursor.execute("select name,age from Roster where species='Bajoran'")
rows=cursor.fetchall()
for row in rows:
    name,age=row
    print(f"Name: {name},Age:{age}")
cursor.execute("delete from Roster where Age>100")
cursor.execute("alter table Roster add rank text;")
data=[
    ("Captain","Benjamin Sisko"),
    ("Lieutenant","Ezri Dax"),
    ("Major","Kira Nerys")
]
cursor.executemany("update Roster set Rank=? where Name=?",data)
cursor.execute(r"select * from Roster order by Age desc")
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()

