from flask import Flask, Blueprint
from flask_cors import CORS

from .cache import cache

from tmdb.views import api, catch_all

app = Flask(__name__, instance_relative_config=False)
CORS(app)


app.config.from_pyfile('config.py', silent=True)
app.register_blueprint(catch_all)
app.register_blueprint(api, url_prefix='/api/v1')
cache.init_app(app)
