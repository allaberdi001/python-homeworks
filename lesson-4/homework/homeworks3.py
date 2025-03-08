

txt=input("txt: ")
l=list(txt)
used=[]
vowels=['a','e','i','o','u','A','E','I','O','U']
i=2
while i<len(l)-1:
    if l[i] not in used and l[i] not in vowels:
        l.insert(i+1,'_')
        used.append(l[i])
        i=i+4
    else:
        inserted=False
        i=i+1
        while not inserted and i<len(l)-1:
            if l[i] not in used and l[i] not in vowels:
                l.insert(i+1,'_')
                used.append(l[i])
                inserted=True
            if inserted:
                i=i+4
            else:
                i=i+1
            
txt="".join(l)
print(txt)
print(used)
