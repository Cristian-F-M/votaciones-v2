from datetime import datetime
import datetime as dt
import uuid

from flask import Blueprint, Response, request
from sqlalchemy.exc import IntegrityError

from app import bcrypt, db
from app.models.Session import Session
from app.models.User import User
from app.utils.form_fields import (
    response_integrity_error,
    user_fields_validations,
    user_required_fields,
)
from app.utils.http import TIME_EXPIRATION_SESSION, json_response
from app.decorators.user import login_required

bp = Blueprint("user", __name__, url_prefix="/user")





@bp.route("/register", methods=["POST"])
def register():
    data = request.json

    if not data:
        return Response(
            json_response({"message": "Invalid data"}),
            status=400,
            mimetype="application/json",
        )

    if not all(key in data for key in user_required_fields):
        return Response(
            json_response({"message": "Missing fields"}),
            status=400,
            mimetype="application/json",
        )

    for field, validation in user_fields_validations.items():
        value = data.get(field, "")

        if not validation["required"] and not value:
            continue

        if not validation["func"](value):
            return Response(
                json_response({"field": field, "message": validation["message"]}),
                status=400,
                mimetype="application/json",
            )

    new_user = User(
        id=uuid.uuid4(),
        name=data["name"],
        lastname=data["lastname"],
        email=data["email"],
        type_document=data["type_document"],
        document=data["document"],
        phone=data["phone"],
        password=bcrypt.generate_password_hash(data["password"]),
        role=1,
    )

    try:
        db.session.add(new_user)
        db.session.commit()

    except IntegrityError as e:
        print(e)
        db.session.rollback()
        message = response_integrity_error(
            error=e,
            sentence="Duplicate entry",
            fields=["users.email", "users.document", "users.phone"],
        )

        return Response(json_response(message), status=400, mimetype="application/json")

    except Exception as e:
        print(e)
        db.session.rollback()
        return Response(
            json_response({"message": "An error occurred, please try again later"}),
            status=500,
            mimetype="application/json",
        )

    return Response(
        json_response({"message": "Registered user"}),
        status=201,
        mimetype="application/json",
    )


@bp.route("/login", methods=["POST"])
def login():

    session_id = request.cookies.get("session_id")
    if session_id:
        return Response(
            json_response({"ok": True, "status": 200, "message": "Already logged in"}),
            status=200,
            mimetype="application/json",
        )

    data = request.json

    if not data:
        return Response(
            json_response({"ok": False, "status": 400, "message": "Invalid data"}),
            status=200,
            mimetype="application/json",
        )

    if not all(key in data for key in ["type_document", "document", "password"]):
        return Response(
            json_response({"ok": False, "status": 400, "message": "Missing fields"}),
            status=200,
            mimetype="application/json",
        )

    user = User.query.filter_by(
        type_document=data["type_document"], document=data["document"]
    ).first()

    if not user:
        return Response(
            json_response({"ok": False, "status": 404, "message": "User not found"}),
            status=200,
            mimetype="application/json",
        )

    if not bcrypt.check_password_hash(user.password, data["password"]):
        return Response(
            json_response(
                {"ok": False, "status": 400, "message": "Invalid credentials"}
            ),
            status=200,
            mimetype="application/json",
        )

    previous_session = Session.query.filter_by(id=user.session).first()
    if not previous_session:
        previous_session = Session(
            id=uuid.uuid4(),
            token=uuid.uuid4(),
            expiration_date=datetime.now()
            + dt.timedelta(seconds=TIME_EXPIRATION_SESSION),
        )
        db.session.add(previous_session)
    else:
        previous_session.expiration_date = datetime.now() + dt.timedelta(
            seconds=TIME_EXPIRATION_SESSION
        )
        previous_session.token = uuid.uuid4()
    user.session = previous_session.id
    db.session.commit()

    response = Response(
        json_response(
            {"ok": True, "status": 100, "data": user.to_dict(), "message": "Logged in"}
        ),
        status=200,
        mimetype="application/json",
    )
    response.set_cookie(
        "session_token",
        previous_session.token,
        expires=previous_session.expiration_date,
    )
    return response


@bp.route("/logout", methods=["POST"])
@login_required
def logout():

    id = request.cookies.get("id")

    user = User.query.get(id)
    session = Session.query.filter_by(user_id=user.id).first()

    session.token = None
    session.expiration_date = None

    db.session.commit()

    response = Response(
        json_response({"message": "Logged out"}),
        status=200,
        mimetype="application/json",
    )
    response.set_cookie("session_token", "", expires=0)
    return response


@bp.route("/validate-token", methods=["GET"])
@login_required
def validate_token():
    return Response(
        json_response({"status": 200, "ok": True, "message": "You are logged in" }),
        status=200,
        mimetype="application/json",
    )
