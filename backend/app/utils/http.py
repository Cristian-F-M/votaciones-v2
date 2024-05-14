import json
from flask import request

ACCEPTED_ORIGINS = ["http://localhost:8080", "http://localhost:5173"]


def json_response(object):
    return json.dumps(object)


def middlware_after_request(response):
    origin = request.origin
    if origin in ACCEPTED_ORIGINS:
        response.headers['Access-Control-Allow-Origin'] = origin
    return response