a=input("Sentence: ").strip()
count=0
for i in range(len(a)):
    if a[i]==" ":
        count +=1
    
print(count+1, " words")