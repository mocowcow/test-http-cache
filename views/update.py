
from flask import Blueprint
from flask import Response
from flask import make_response

from data_module import api as data_api

bp = Blueprint("update", __name__)


@bp.route("/update/<new_data>")
def modify_data(new_data) -> Response:
    data_api.update(new_data)
    resp = make_response("ok", 200)
    return resp
