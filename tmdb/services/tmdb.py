import requests
from tmdb import config



class TMDBService:

    MOVIE_BASE_URL = f'{config.TMDB_BASE_URL}/movie'
    BASE_QUERY_PARAMS = f'api_key={config.TMDB_API_KEY}&language=en-US'

    @staticmethod
    def get_upcoming_movie_list():
        url = f'{TMDBService.MOVIE_BASE_URL}/upcoming'
        params = f'{TMDBService.BASE_QUERY_PARAMS}&page=1'

        return requests.get(url, params=params).json()
