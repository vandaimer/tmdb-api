from flask import Blueprint, request, jsonify
import time

from .health_check import HealthCheck
from .movie import Movie


api = Blueprint('api', __name__)
catch_all = Blueprint('catch_all', 'catch_all')


@catch_all.route('/', defaults={'path': ''})
@catch_all.route('/<path:path>')
def catch_all_view(path):
    return {
        'path': path,
        'status': 'notImplemented',
        'now':  time.time(),
    }

@api.route('/healthcheck', methods=['GET'])
def call_healt_check_view():
    return HealthCheck.get()


@api.route('/movie/upcoming', methods=['GET'])
def call_movie_upcoming_list():
    page = request.args.get('page', 1)
    return jsonify(Movie.get_upcoming_list(page=page))
