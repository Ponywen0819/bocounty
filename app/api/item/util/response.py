from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def item_not_found():
    raise HTTPException(response=make_response(jsonify({
        "message": "item not exist or accessible"
    }), 404))