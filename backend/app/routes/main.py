from flask import Blueprint
from flask import request, Response
import json

bp = Blueprint("main", __name__)


@bp.route("/data")
def index():
    data = {"data": {"more_data": 1}}
    response = Response(json.dumps(data), status=200, mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
