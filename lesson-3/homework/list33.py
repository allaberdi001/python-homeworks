l=input("Enter elements of a list with space in between: ").strip().split()
elm=input("what element: ")
collection=[l.index(elm)]
i=l.index(elm)+1
try:
    while True:
        collection.append(l.index(elm,i))
        i=l.index(elm,i)+1
except:
    print(collection)