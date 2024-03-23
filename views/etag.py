
from flask import Blueprint
from flask import Response
from flask import make_response
from flask import request

from data_module import api as data_api

bp = Blueprint("etag", __name__)


@bp.route("/last_modified")
def get_time() -> Response:
    ims = request.headers.get("If-Modified-Since")
    if data_api.is_modified_since(ims):
        return make_response("", 304)

    data = data_api.get()
    resp = make_response(data, 200)
    resp.headers["Cache-Control"] = "no-cache"
    resp.headers["Last-Modified"] = data_api.last_modified

    return resp
