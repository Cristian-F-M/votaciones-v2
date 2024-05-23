from functools import wraps
from flask import request, Response
from app.utils.http import json_response
from app.models.Session import Session
from app.models.User import User
import json

def login_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        user = json.loads(request.cookies.get("user"))
        session_token = request.cookies.get("session_token")

        user = User.query.get(user['id'])
        
        if user and user.session:
            session = Session.query.filter_by(id=user.session).first()
            if session and session.token == session_token:
                return func(*args, **kwargs)

        return Response(
            json_response({ "ok": False, "status": 401, "message": "You need to be logged in to access this page" }),
            status=401,
            mimetype="application/json",
        )

    return decorator
