import configparser
import requests


config = configparser.ConfigParser()
config.read('config.ini')

key=config['DEFAULT']['key']
token=config['DEFAULT']['token']

url = f"https://api.themoviedb.org/3/movie/550?api_key={key}"

poster_sizes=[
      "w92",
      "w154",
      "w185",
      "w342",
      "w500",
      "w780",
      "original"
    ]

def get_popular_movies(movie_num: int = 8) -> dict:
    assert movie_num > 1
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json;charset=utf-8"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['results'][:movie_num]

def get_poster_url(poster_api_path, size: str="w342") -> str:
    # assert size in poster_sizes
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    if 'cast' in response.json():
        return response.json()["cast"]
    else:
        return []

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

