from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def not_login():
    raise HTTPException(response=make_response(jsonify({
        "message": "user not login"
    }), 403))

def no_permission():
    raise HTTPException(response=make_response(jsonify({
        "message": "user is not administrator"
    }), 403))
