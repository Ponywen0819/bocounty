from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def success(addition: dict = None):
    if addition is None:
        addition = dict()

    return make_response(jsonify({
        "message": "OK",
        **addition
    }), 200)


def wrong_format(message: str = "wrong format"):
    raise HTTPException(response=make_response(jsonify({
        "message": message
    }), 400))


def missing_required(message: str = "missing required column"):
    raise HTTPException(response=make_response(jsonify({
        "message": message
    }), 400))

def not_login(message: str = "user no login"):
    raise HTTPException(response=make_response(jsonify({
        "message": message
    }), 403))


def not_found(message: str = "user no found"):
    raise HTTPException(response=make_response(jsonify({
        "message": message
    }), 404))


