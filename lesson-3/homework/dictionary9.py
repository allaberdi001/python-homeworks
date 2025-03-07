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
dict1={}
def func(dict):
    if len(dict)==0:
        return "no element"
    else:
        return "element(s) exist"
print(func(dict))
print(func(dict1))