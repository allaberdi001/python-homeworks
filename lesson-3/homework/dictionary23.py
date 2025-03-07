dict1={
    '1':1,
    '3':3,
    '6':6,
    '2':2,
}
dict2={
    '1':1,
    '4':4,
    '8':8,
}
s1=set(dict1.keys())
s2=set(dict2.keys())
if len(s1&s2)==0:
    print("no keys in common")
else:
    print("some keys in common")