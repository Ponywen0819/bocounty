from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def conflict():
    raise HTTPException(response=make_response(jsonify({
        "message": "student id conflict"
    }), 400))
