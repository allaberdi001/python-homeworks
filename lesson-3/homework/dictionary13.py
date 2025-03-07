dict = {
    "genre": "Jazz",
    "artist": "Miles Davis",
    "album": "Kind of Blue",
    "release_year": 1959,
    "famous_song": "So What",
    "duration_minutes": 9.22,
    "live_performance": False,
} 
new_dict={}
for key, value in dict.items():
    new_dict[value]=key
print(new_dict)
