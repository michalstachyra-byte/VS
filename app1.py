import csv
from flask import Flask
from flask_restful import Api, Resource
from models import Movie

app = Flask(__name__)
api = Api(app)

class Movies(Resource):
    def get(self):
        movies = []

        with open('movies.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # nagłówek

            for row in reader:
                movie_id = row[0]
                title = row[1]
                genres = row[2]

                movie = Movie(movie_id, title, genres)
                movies.append(movie.__dict__)

        return movies

api.add_resource(Movies, '/movies')

if __name__ == '__main__':
    app.run(debug=True)
