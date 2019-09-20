from flask import Blueprint, request, jsonify

from .health_check import HealthCheck
from .movie import Movie


api = Blueprint('api', __name__)


@api.route('/healthcheck', methods=['GET'])
def call_healt_check_view():
    return HealthCheck.get()


@api.route('/movies', methods=['GET'])
def call_movies_upcoming_list():
    return jsonify(Movie.get_upcoming_list())
