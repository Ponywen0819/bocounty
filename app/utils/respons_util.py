from werkzeug.exceptions import BadRequest, NotFound, Forbidden, Unauthorized, HTTPException
from flask import make_response, jsonify, abort
from app.utils.enum_util import APIStatusCode


def success(addition: dict = None):
    if addition is None:
        addition = dict()

    return jsonify({
        "message": "ok",
        **addition
    })


def incorrect_login_info():
    raise HTTPException(response=make_response(jsonify({
        "message": "incorrect student id or password"
    }), 400))


def missing_required():
    raise HTTPException(response=make_response(jsonify({
        "message": "missing required column"
    }), 400))


def wrong_format():
    raise HTTPException(response=make_response(jsonify({
        "message": "format not matched"
    }), 400))


def not_verified():
    raise HTTPException(response=make_response(jsonify({
        "message": "mail verified is not completed"
    }), 401))


def no_permission():
    raise HTTPException(response=make_response(jsonify({
        "message": 'have no permission'
    }), 403))


def not_found():
    raise HTTPException(response=make_response(jsonify({
        "message": "request resource not found"
    }), 404))


def make_error_response(code: APIStatusCode, reason: str = ''):
    return make_response(jsonify({
        'status': code.value.api_code,
        'reason': reason
    }), code.value.http_code)
