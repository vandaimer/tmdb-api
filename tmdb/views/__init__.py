from flask import Blueprint

from .health_check import HealthCheck


api = Blueprint('api', __name__)


@api.route('/healthcheck', methods=['GET'])
def call_healt_check_view():
    return HealthCheck.get()
