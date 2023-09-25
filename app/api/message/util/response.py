from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def not_valid_member(message: str = "user is not member of this chatroom "):
    raise HTTPException(response=make_response(jsonify({
        "message": message
    }), 422))
