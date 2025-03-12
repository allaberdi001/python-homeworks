with open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-6\homework\sample.txt","r") as f:
    text=f.read().replace(",","").replace(".","").replace("\n"," ").strip().replace("  "," ").lower()
l=text.split()
freq={}
for elm in l:
    if elm not in freq.keys():
        freq[elm]=1
    else:
        freq[elm]=freq[elm]+1
freq=dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))
print("Total words: ",len(l))
print("Top 5 most common words:")
for i in range(5):
    print(f"{list(freq.keys())[i]} - {freq[list(freq.keys())[i]]} times")
with open(r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-6\homework\word_count_report.txt","w") as f:
    f.write("Word Count Report\n")
    f.write(f"Total Words: {len(l)}\nTop 5 Words:\n")
    for i in range(5):
        f.write(f"{list(freq.keys())[i]} - {freq[list(freq.keys())[i]]} times\n")

