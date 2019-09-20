from tmdb.services import TMDBService


class Movie:
    @staticmethod
    def get_upcoming_list():
        movies = TMDBService.get_upcoming_movie_list()
        movies = [Movie.build_movie(movie) for movie in movies['results']]

        return {
                'items': movies,
        }

    @staticmethod
    def build_movie(movie):
        poster = movie.get('poster_path')
        backdrop = movie.get('backdrop_path')

        return {
            'title': movie.get('title'),
            'release_date': movie.get('release_date'),
            'poster': TMDBService.get_image_url(poster),
            'backdrop': TMDBService.get_image_url(backdrop),
        }
