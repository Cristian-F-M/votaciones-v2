from flask import Blueprint, request, Response
from app.utils.http import json_response
from app.utils.http import json_response, ACCEPTED_ORIGINS, ACCEPTED_METHODS
from app.models.Type_document import Type_document

bp = Blueprint("resources", __name__, url_prefix="/resources")

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


@bp.route("/types_document", methods=["GET"])
def get_types_document():

    types_document = Type_document.query.all()

    types_document = [d.to_dict() for d in types_document]
    print(types_document)

    return Response(
        json_response(types_document),
        status=200,
        mimetype="application/json",
    )
