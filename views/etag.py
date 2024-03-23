
from flask import Blueprint
from flask import Response
from flask import make_response
from flask import request

from data_module import api as data_api

bp = Blueprint("etag", __name__)


@bp.route("/etag")
def get_time() -> Response:
    etag = request.headers.get("If-None-Match")
    if data_api.is_etag_match(etag):
        return make_response("", 304)

    data = {
        "resp count": f"這是第{data_api.count()}次回應",
        "data": data_api.shared_data,
    }
    resp = make_response(data, 200)
    resp.headers["Cache-Control"] = "no-cache"
    resp.headers["Etag"] = data_api.etag

    return resp
