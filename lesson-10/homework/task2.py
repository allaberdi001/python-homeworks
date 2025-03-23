import requests
import random

API_KEY = "f4192929fd7af1d7a7b3ec940ea7064a" 
BASE_URL = "https://api.themoviedb.org/3"

def get_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json()["genres"]
        return {genre["name"].lower(): genre["id"] for genre in genres}
    else:
        print("Error fetching genres.")
        return {}

def get_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()["results"]
        return movies if movies else None
    else:
        print("Error fetching movies.")
        return None

def recommend_movie():
    genres = get_genres()
    if not genres:
        return
    print("\nAvailable genres:")
    for genre in genres.keys():
        print(f"- {genre.capitalize()}")

    user_genre = input("\nEnter a movie genre: ").strip().lower()

    if user_genre in genres:
        genre_id = genres[user_genre]
        movies = get_movies_by_genre(genre_id)

        if movies:
            movie = random.choice(movies) 
            print(f"\nRecommended Movie: {movie['title']}")
            print(f"Release Date: {movie['release_date']}")
            print(f"Rating: {movie['vote_average']}/10")
            print(f"Overview: {movie['overview']}\n")
        else:
            print("No movies found in this genre.")
    else:
        print("Invalid genre. Please try again.")

recommend_movie()