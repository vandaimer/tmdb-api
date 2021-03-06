from tmdb.services import TMDBService
from .genre import Genre


class Movie:
    @staticmethod
    def get_upcoming_list(page):
        result = TMDBService.get_upcoming_movie_list(page=page)

        if result.get('errors'):
            return {
                'items': [],
                'page': 1,
                'total_pages': 1,
                'total_results': 0
            }

        movies = [Movie.build_movie(movie) for movie in result['results']]

        return {
            'items': movies,
            'page': result['page'],
            'total_pages': result['total_pages'],
            'total_results': result['total_results'],
        }

    @staticmethod
    def build_movie(movie):
        poster = movie.get('poster_path')
        backdrop = movie.get('backdrop_path')
        genre_ids = movie.get('genre_ids')

        built_movie = {
            'title': movie.get('title'),
            'release_date': movie.get('release_date'),
            'overview': movie.get('overview'),
            'genres': [Genre.get_genre_by_id(genre_id)
                       for genre_id in genre_ids],
        }

        if backdrop:
            built_movie['backdrop'] = TMDBService.get_image_url(backdrop)

        if poster:
            built_movie['poster'] = TMDBService.get_image_url(poster)

        return built_movie
