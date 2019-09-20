import os


DEBUG = os.getenv("FLASK_DEBUG") == "DEV"
TMDB_BASE_URL = os.getenv("TMDB_BASE_URL")
