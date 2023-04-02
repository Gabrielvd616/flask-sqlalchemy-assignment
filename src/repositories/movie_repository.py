from ..models import Movie
from app import db


class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        query = Movie.select()
        exe = db.execute(query)  # executing the query
        return exe

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        query = Movie.select(['id']).where(Movie.columns.id == movie_id)
        exe = db.execute(query)  # executing the query
        return exe

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        query = db.insert(Movie).values(title=title, director=director, rating=rating)
        exe = db.execute(query)  # executing the query
        return exe

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        query = Movie.select(['title']).where(Movie.columns.title == title)
        exe = db.execute(query)  # executing the query
        return exe


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
