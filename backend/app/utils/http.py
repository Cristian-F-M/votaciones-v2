import json

ACCEPTED_ORIGINS = ["http://localhost:8080", "http://localhost:5173"]


def json_response(object):
    return json.dumps(object)
