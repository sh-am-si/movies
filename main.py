from flask import Flask, render_template
from tmdb_client import get_popular_movies

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def homepage():
    movies = get_popular_movies()
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)