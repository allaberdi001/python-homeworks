dict = {
    "genre": "Jazz",
    "artist": "Miles Davis",
    "album": "Kind of Blue",
    "release_year": '1959',
    "instruments": ["Trumpet", "Piano", "Bass", "Drums"],
    "famous_song": "So What",
    "duration_minutes": '9.22',
    "labels": ["Columbia Records"],
    "live_performance": False,
    "ratings": {"Pitchfork": 10, "Rolling Stone": 5},
    "some_other_year":'1959'
} 
value=input("what value: ")
count=0
for i in dict.keys():
    if dict[i]==value:
        count=count+1
print(count)