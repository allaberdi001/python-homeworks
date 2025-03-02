a=input("Kiriting: ").lower().replace(" ","")
vowel_count=0
consonant_count=0
for i in range(len(a)):
    if a[i]=='a' or a[i]=='o' or a[i]=='i' or a[i]=='u' or a[i]=='e':
        vowel_count +=1
    else:
        consonant_count +=1
print(vowel_count," vowels")
print(consonant_count, "consonants")