Keys= ['genre', 'artist', 'album', 'release_year', 'instruments', 'famous_song', 'duration_minutes', 'labels', 'live_performance', 'ratings']
Values= ['Jazz', 'Miles Davis', 'Kind of Blue', 1959, ['Trumpet', 'Piano', 'Bass', 'Drums'], 'So What', 9.22, ['Columbia Records'], False, {'Pitchfork': 10, 'Rolling Stone': 5}]
dict={}
for i in range(len(Keys)):
    dict[Keys[i]]=Values[i]
print(dict)