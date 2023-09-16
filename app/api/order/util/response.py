from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def not_found():
    pass


def missing_required():
    raise HTTPException(response=make_response(jsonify({
        "message": "missing required column"
    }), 400))


def wrong_format():
    raise HTTPException(response=make_response(jsonify({
        "message": "wrong data format"
    }), 400))


def date_in_past():
    raise HTTPException(response=make_response(jsonify({
        "message": "date is in the past"
    }), 400))
