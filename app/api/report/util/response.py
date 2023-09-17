from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def self_report():
    raise HTTPException(response=make_response(jsonify({
        "message": "could not self report"
    }), 409))