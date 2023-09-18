from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def date_in_past():
    raise HTTPException(response=make_response(jsonify({
        "message": "date is in the past"
    }), 400))
