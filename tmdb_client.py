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

def get_popular_movies() -> dict:
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json;charset=utf-8"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size: str="w342") -> str:
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

