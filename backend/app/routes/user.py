from flask import Blueprint
from flask import request, Response
from app.utils.http import json_response, ACCEPTED_ORIGINS, ACCEPTED_METHODS
from app.utils.form_fields import (
    user_required_fields,
    user_fields_validations,
    response_integrity_error,
)
from app.models.User import User
from app import db, bcrypt
import uuid
from sqlalchemy.exc import IntegrityError


bp = Blueprint("user", __name__)

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




@bp.route("/user/register", methods=["POST"])
def user_register():
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
        password = bcrypt.generate_password_hash(data["password"]),
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

    return Response(json_response({"message": "Registered user" }), status=200, mimetype="application/json")
