import requests
from tmdb import config


class TMDBService:

    MOVIE_BASE_URL = f'{config.TMDB_API_BASE_URL}/movie'
    GENRE_BASE_URL = f'{config.TMDB_API_BASE_URL}/genre/movie/list'
    IMAGE_BASE_URL = f'{config.TMDB_IMAGE_BASE_URL}/w500'
    BASE_QUERY_PARAMS = f'api_key={config.TMDB_API_KEY}&language=en-US'

    @staticmethod
    def get_upcoming_movie_list(page):
        url = f'{TMDBService.MOVIE_BASE_URL}/upcoming'
        params = f'{TMDBService.BASE_QUERY_PARAMS}&page={page}'

        return requests.get(url, params=params).json()

    @staticmethod
    def get_genre_list():
        url = TMDBService.GENRE_BASE_URL
        params = TMDBService.BASE_QUERY_PARAMS

        return requests.get(url, params=params).json()

    @staticmethod
    def get_image_url(image_hash):
        return f'{TMDBService.IMAGE_BASE_URL}/{image_hash}'
