import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver =webdriver.Chrome()
time.sleep(2)
driver.get(r"https://www.demoblaze.com/")
categories=driver.find_elements(By.ID,"itemc")
categories[1].click()
time.sleep(2)


l=[]
cards=driver.find_elements(By.CLASS_NAME, "mb-4")
for card in cards:
    title=card.find_element(By.CLASS_NAME, "hrefch").text
    price=card.find_element(By.TAG_NAME,"h5").text
    description=card.find_element(By.CLASS_NAME, "card-text").text
    item={"name":title,"price":price,"description":description}
    l.append(item)
next=driver.find_element(By.ID, "next2")
next.click()
time.sleep(2)


cards=driver.find_elements(By.CLASS_NAME, "mb-4")
for card in cards:
    title=card.find_element(By.CLASS_NAME, "hrefch").text
    price=card.find_element(By.TAG_NAME,"h5").text
    description=card.find_element(By.CLASS_NAME, "card-text").text
    item={"name":title,"price":price,"description":description}
    l.append(item)

print(l)