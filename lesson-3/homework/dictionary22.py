dict1={
    '1':1,
    '3':3,
    '6':6,
    '2':2,
}
dict2={}
for key in dict1.keys():
    if dict1[key]>=3:
        dict2[key]=dict1[key]
print(dict2)