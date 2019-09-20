from flask import Blueprint, request, jsonify

from .health_check import HealthCheck
from .movie import Movie


api = Blueprint('api', __name__)


@api.route('/healthcheck', methods=['GET'])
def call_healt_check_view():
    return HealthCheck.get()


@api.route('/movie/upcoming', methods=['GET'])
def call_movie_upcoming_list():
    page = request.args.get('page', 1)
    return jsonify(Movie.get_upcoming_list(page=page))
