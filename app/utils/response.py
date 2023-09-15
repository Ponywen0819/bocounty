from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def success(addition: dict = None):
    if addition is None:
        addition = dict()

    raise HTTPException(response=make_response(jsonify({
        "message": "OK"
    }), 200))



