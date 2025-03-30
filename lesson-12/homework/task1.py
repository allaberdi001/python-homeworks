import requests
from bs4 import BeautifulSoup

file=r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-12\homework\weather.html"
with open(file,"r",encoding="utf-8") as f:
    html_content=f.read()

soup=BeautifulSoup(html_content,"html.parser")

all_info=soup.find_all("td")
for i in range(len(all_info)//3):
    print(f"{all_info[0+i*3].text}: temperature: {all_info[1+i*3].text} and condition: {all_info[2+i*3].text}")

highest=int(all_info[1].text[:-2])
total=0
for i in range(len(all_info)//3):
    total=total+int(all_info[i*3+1].text[:-2])
    if int(all_info[i*3+1].text[:-2])>highest:
        highest=int(all_info[i*3+1].text[:-2])
print("Highest temperature is ",highest,"°C")
sunny=[]
for i in range(len(all_info)//3):
    if all_info[i*3+2].text=="Sunny":
        sunny.append(all_info[i*3].text)
print(", ".join(sunny), " was/were sunny days")
print("Average temperature was: ",total//(len(all_info)//3), "°C")