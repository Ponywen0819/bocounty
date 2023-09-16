from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def conflict():
    raise HTTPException(response=make_response(jsonify({
        "message": "student id conflict"
    }), 400))


def missing_required():
    raise HTTPException(response=make_response(jsonify({
        "message": "missing required column"
    }), 400))


def not_found():
    raise HTTPException(response=make_response(jsonify({
        "message": "user not found"
    }), 404))
