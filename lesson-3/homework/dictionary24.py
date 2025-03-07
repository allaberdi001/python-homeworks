tuple_data = (("name", "Allaberdi"), ("age", 18), ("city", "Ulsan"))
dict1={}
for i in range(len(tuple_data)):
    dict1[tuple_data[i][0]]=tuple_data[i][1]
print(dict1)