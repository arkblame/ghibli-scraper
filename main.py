from flask import Flask, render_template
from flask_caching import Cache

from scraper import FILMS, PEOPLE
from scraper.getter import get_cast_for_movie, get_all_data

app = Flask("Ghibli-scrapper")
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route("/movies")
@cache.cached(timeout=60)
def present_movies():
    movies = get_all_data(FILMS)
    people = get_all_data(PEOPLE)

    for movie in movies:
        get_cast_for_movie(movie, people)

    return render_template('movies.html', movies=movies)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
