from functools import wraps
from flask import request, Response
from app.utils.http import json_response
from app.models.Session import Session
from app.models.User import User


def login_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        id = request.cookies.get("id")
        session_token = request.cookies.get("session_token")

        print("#"*100)
        print(id, session_token)
        print("#"*100)
        print(request.cookies)

        user = User.query.get(id)
        
        if user.session:
            session = Session.query.filter_by(id=user.session).first()
            if session and session.token == session_token:
                return func(*args, **kwargs)

        return Response(
            json_response({"message": "You need to be logged in to access this page"}),
            status=401,
            mimetype="application/json",
        )

    return decorator
