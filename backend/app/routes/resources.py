from flask import Blueprint, Response
from app.utils.http import json_response
from app.models.Type_document import Type_document

bp = Blueprint("resources", __name__, url_prefix="/resources")


@bp.route("/types_document", methods=["GET"])
def get_types_document():

    types_document = Type_document.query.all()

    types_document = [d.to_dict() for d in types_document]

    data = {"status": 200, "ok": True, "data": types_document}

    return Response(
        json_response(data),
        status=200,
        mimetype="application/json",
    )
