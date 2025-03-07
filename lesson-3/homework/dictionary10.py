def my_function(dict,key):
    value=dict.get(key,None)
    if value==None:
        return "no such key exist"
    else:
        return (key,value)
dict = {
    "genre": "Jazz",
    "artist": "Miles Davis",
    "album": "Kind of Blue",
    "release_year": 1959,
    "instruments": ["Trumpet", "Piano", "Bass", "Drums"],
    "famous_song": "So What",
    "duration_minutes": 9.22,
    "labels": ["Columbia Records"],
    "live_performance": False,
    "ratings": {"Pitchfork": 10, "Rolling Stone": 5}
} 

print(my_function(dict, 'genre'))
print(my_function(dict, 'good boy'))