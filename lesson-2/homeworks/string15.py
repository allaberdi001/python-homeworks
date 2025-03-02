a=" "+input("Sentence: ")
acronym=""
for i in range(len(a)):
    if a[i]==" " and a[i+1] != " ":
        acronym=acronym+a[i+1]
print(acronym)