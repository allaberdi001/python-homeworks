dict1={
    1:'1',
    3:'3',
    6:"6",
    2:'2',
}
sorted_dict=dict(sorted(dict1.items(), key=lambda item:item[1]))
print(sorted_dict)