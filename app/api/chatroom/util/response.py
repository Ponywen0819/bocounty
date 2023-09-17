from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify

def already_exist():
    raise HTTPException(response=make_response(jsonify({
        "message": "user has already participate"
    }), 409))

def not_member():
    raise HTTPException(response=make_response(jsonify({
        "message": "user is not chatroom member"
    }), 404))


def not_owner():
    raise HTTPException(response=make_response(jsonify({
        "message": "user is not order owner"
    }), 409))

def is_owner():
    raise HTTPException(response=make_response(jsonify({
        "message": "user is order owner"
    }), 422))

