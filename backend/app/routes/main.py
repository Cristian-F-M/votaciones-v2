from flask import Blueprint
from flask import request, Response
from app.utils.http import json_response, ACCEPTED_ORIGINS, ACCEPTED_METHODS

bp = Blueprint("main", __name__)


@bp.after_request
def middlware_after(response):
    origin = request.origin
    method = request.method

    if method in ACCEPTED_METHODS:
        response.headers["Access-Control-Allow-Methods"] = method
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    if origin in ACCEPTED_ORIGINS or not origin:
        response.headers["Access-Control-Allow-Origin"] = origin
    return response


@bp.route("/test", methods=["GET"])
def test():
    data = json_response({"res": "All ok"})
    response = Response(data, status=200, mimetype="application/json")
    return response
