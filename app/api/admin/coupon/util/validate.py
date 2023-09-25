from app.utils.response import missing_required, wrong_format, not_found
from app.utils.time_util import str2date, get_current
from app.database.util import get

from .coupon import CreateCoupon
from flask import request
from datetime import datetime
from .response import date_in_past


def validate_create_payload():
    payload: dict = request.json

    try:
        CreateCoupon(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()


def validate_close_time():
    payload: dict = request.json

    close_time = payload.get("close_time")

    if close_time is None:
        return

    if type(close_time) != str:
        wrong_format()

    _validate_iso_format(close_time)
    _validate_date_correct(close_time)

def validate_count():
    payload: dict = request.json

    count = payload.get("count")
    if count < 1:
        wrong_format()


def validate_price():
    payload: dict = request.json

    price = payload.get("price")
    if price < 1:
        wrong_format()


def validate_name():
    payload: dict = request.json

    name = payload.get("name")
    while len(name) > 0:
        if name[0] == " ":
            name = name[1:]
        else:
            break

    if name == "":
        wrong_format()


def validate_describe():
    payload: dict = request.json

    describe = payload.get("describe")
    while len(describe) > 0:
        if describe[0] == " ":
            describe = describe[1:]
        else:
            break

    if describe == "":
        wrong_format()

def validate_coupon_exist(coupon_id: str):
    coupons = get('coupon_type',{
        "id": coupon_id
    })

    if len(coupons) != 1:
        not_found("coupon not found")



def _validate_iso_format(value: str):
    try:
        datetime.fromisoformat(value)
    except ValueError:
        raise wrong_format()


def _validate_date_correct(value: str):
    current = get_current()
    date = str2date(value)

    if date < current:
        date_in_past()
