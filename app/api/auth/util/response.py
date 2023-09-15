from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def wrong_format():
    raise HTTPException(response=make_response(jsonify({
        "message": "wrong format"
    }), 400))


def missing_required():
    raise HTTPException(response=make_response(jsonify({
        "message": "missing required column"
    }), 400))


def not_found():
    raise HTTPException(response=make_response(jsonify({
        "message": "user no verified"
    }), 401))


def not_verified():
    raise HTTPException(response=make_response(jsonify({
        "message": "user no verified"
    }), 403))
