from flask import Blueprint
from flask import request, Response
from app.utils.http import json_response, middlware_after_request
from app.models.User import User


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




@bp.route("/user/register", methods=["POST"])
def user_register():
    data = request.json
    return Response(json_response(data), status=200, mimetype='application/json')