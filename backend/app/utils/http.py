import json

ACCEPTED_ORIGINS = ["http://localhost:8080", "http://localhost:5173"]
ACCEPTED_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
TIME_EXPIRATION_SESSION = 60 * 60 * 4 # 4 hours  

def json_response(object):
    return json.dumps(object)
