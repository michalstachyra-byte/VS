class Movie:
    def __init__(self, movie_id, title, genres):
        self.id = movie_id
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movieId = movie_id
        self.imdbId = imdb_id
        self.tmdbId = tmdb_id


class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.tag = tag
        self.timestamp = timestamp
