import os


DEBUG = os.getenv("FLASK_DEBUG") == "DEV"
CACHE_TYPE = os.getenv("CACHE_TYPE", "simple")
TMDB_API_BASE_URL = os.getenv("TMDB_API_BASE_URL")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_IMAGE_BASE_URL = os.getenv('TMDB_IMAGE_BASE_URL')
