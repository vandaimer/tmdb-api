from tmdb.services import TMDBService
from tmdb.cache import cache


ONE_DAY_TIMEOUT = 60 * 60 * 24


class Genre:
    @staticmethod
    def get_genre_by_id(genre_id):
        genres = Genre.get_genres()
        return genres.get(genre_id, 'Unknown')

    @staticmethod
    @cache.cached(timeout=ONE_DAY_TIMEOUT, key_prefix='all_genres')
    def get_genres():
        genre_list = TMDBService.get_genre_list()
        return Genre.build_genre_structure(genre_list['genres'])

    @staticmethod
    def build_genre_structure(genre_list):
        return { genre['id']: genre['name'] for genre in genre_list }
