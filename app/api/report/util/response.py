from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def self_report():
    raise HTTPException(response=make_response(jsonify({
        "message": "could not self report"
    }), 406))


def reported():
    raise HTTPException(response=make_response(jsonify({
        "message": "user already reported the same order"
    }), 409))
