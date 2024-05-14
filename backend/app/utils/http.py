import json

ACCEPTED_ORIGINS = ["http://localhost:8080", "http://localhost:5173"]
ACCEPTED_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

def json_response(object):
    return json.dumps(object)
