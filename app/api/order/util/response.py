from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def missing_required():
    raise HTTPException(response=make_response(jsonify({
        "message": "missing or unknown column"
    }), 400))


def wrong_format():
    raise HTTPException(response=make_response(jsonify({
        "message": "wrong data format"
    }), 400))


def date_in_past():
    raise HTTPException(response=make_response(jsonify({
        "message": "date is in the past"
    }), 400))


def close_after_exec():
    raise HTTPException(response=make_response(jsonify({
        "message": "close order before execute"
    }), 400))


def no_enough_coin():
    raise HTTPException(response=make_response(jsonify({
        "message": "coin not enough"
    }), 402))


def no_permission():
    raise HTTPException(response=make_response(jsonify({
        "message": "have no permission"
    }), 403))


def not_found():
    raise HTTPException(response=make_response(jsonify({
        "message": "order not found"
    }), 404))


def conflict_id():
    raise HTTPException(response=make_response(jsonify({
        "message": "order has duplicate id"
    }), 500))
