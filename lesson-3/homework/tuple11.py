t=tuple(input("tuple 1:Enter elements with space in between: ").strip().split())
elm=input("what element: ")
collection=[t.index(elm)]
i=t.index(elm)+1
try:
    while True:
        collection.append(t.index(elm,i))
        i=t.index(elm,i)+1
except:
    print(collection)