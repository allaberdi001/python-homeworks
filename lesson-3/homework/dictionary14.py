dict = {
    "genre": "Jazz",
    "artist": "Miles Davis",
    "album": "Kind of Blue",
    "famous_song": "So What",
    "good":"So What"
} 

this_value=input("enter value: ")
keys=[]
for key, value in dict.items():
    if value==this_value:
        keys.append(key)
print(keys)