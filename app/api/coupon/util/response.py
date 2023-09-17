from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def no_enough_coin():
    raise HTTPException(response=make_response(jsonify({
        "message": "coin not enough"
    }), 402))
