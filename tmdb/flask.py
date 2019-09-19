from flask import Flask


from tmdb.views import api

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py', silent=True)
app.register_blueprint(api, url_prefix='/api/v1')
