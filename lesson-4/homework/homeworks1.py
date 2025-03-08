list1 = [1, 2, 3]
list2 = [4, 2, 6]
list3=[]
for elm in list1:
    if elm not in list2:
        list3.append(elm)
for elm in list2:
    if elm not in list1:
        list3.append(elm)
print(list3)