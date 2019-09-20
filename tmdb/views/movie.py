from tmdb.services import TMDBService


class Movie:
    @staticmethod
    def get_upcoming_list():
        result = TMDBService.get_upcoming_movie_list()
        movies = [Movie.build_movie(movie) for movie in result['results']]

        return {
            'items': movies,
            'page': result['page'],
            'total_pages': result['total_pages'],
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
