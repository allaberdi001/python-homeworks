from datetime import datetime
current_year = datetime.now().year


name=input("Name: ")
year=int(input("Birth Year: "))
print(name, " you are ", current_year - year, " years old")
