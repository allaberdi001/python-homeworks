import sqlite3
with sqlite3.connect("library.db") as conn:
    cursor=conn.cursor()
    cursor.execute("""create table Books(
                   Title Text,
                   Author text,
                   Year_Published integer,
                   Genre text
                   )
                   """)
    data=[
        ("To Kill a Mockingbird","Harper Lee",1960,	"Fiction"),
        ("1984",	"George Orwell",	1949,	"Dystopian"),
        ("The Great Gatsby",	"F. Scott Fitzgerald",	1925,	"Classic")
    ]
    cursor.executemany("insert into Books(Title,Author,year_published,genre) values(?,?,?,?)",data)
    cursor.execute("update books set year_published=1950 where title='1984'")
    cursor.execute("select title,author from books where genre='Dystopian'")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    cursor.execute("delete from books where year_published<1950")
    data2=[
        (4.8,"To Kill a Mockingbird"),
        (4.7,"1984"),
        (4.5,"The Great Gatsby")
    ]
    cursor.execute("alter table books add Rating float")
    cursor.executemany("update books set rating=? where title=?",data2)
    cursor.execute("select * from books order by year_published asc")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
