import requests
from bs4 import BeautifulSoup
import csv
import sqlite3
url=r"https://realpython.github.io/fake-jobs"

db="jobs.db"
def create_database():
    with sqlite3.connect(db) as conn:
        cursor=conn.cursor()
        cursor.execute("""
        create table if not exists jobs(
            job_title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(job_title, company, location)
            )
        """)
        conn.commit()
def scrape_data():
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    all_jobs=soup.find_all("div",class_="card-content")
    jobs=[]
    for job in all_jobs:
        job_title=job.find("h2",class_="title is-5").text.strip()
        company_name=job.find("h3",class_="subtitle is-6 company").text.strip()
        location=job.find("p",class_="location").text.strip()
        description = job.find("p",class_="location").text.strip()
        print(description)
        application_link=job.find("a", class_="card-footer-item")["href"]
        jobs.append((job_title,company_name,location,description,application_link))
    print(jobs)
    return jobs
def insert(jobs):
    with sqlite3.connect(db) as conn:
        cursor=conn.cursor()
        cursor.executemany("insert or ignore into jobs (job_title,company,location,description,application_link) values(?,?,?,?,?)",jobs)
        conn.commit()
def filter(location=None,company=None):
    with sqlite3.connect(db) as conn:
        cursor=conn.cursor()
        query="select * from jobs where 1=1"
        p=[]
        if location:
            query=query+" and location like ?"
            p.append(f"{location}")
        if company:
            query=query+"and company like ?"
            p.append(f"{company}")
        cursor.execute(query,p)
        data=cursor.fetchall()
        return data
def export(data):
    with open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-12\homework\filtered.csv", "w", encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows(data)
def main():
    create_database()
    jobs=scrape_data()
    insert(jobs)

    print("****filter*****")
    data=filter(location="Stewartbury, AA")
    print(data)
    export(data)
main()


