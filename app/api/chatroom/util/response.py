from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify

def already_exist():
    raise HTTPException(response=make_response(jsonify({
        "message": "user has already participate"
    }), 409))