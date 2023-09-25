from flask import Response
from datetime import datetime, timedelta, timezone
from app.utils.jwt_util import jwt_encode


def with_jwt(res: Response, user: dict) -> Response:
    expires = datetime.now(tz=timezone(timedelta(hours=8))) + timedelta(days=2)

    encoded = jwt_encode({
        "id": user["id"],
        "exp": expires
    })

    res.set_cookie('user_token', encoded, expires=expires)

    return res


def without_jwt(res: Response) -> Response:
    res.set_cookie('user_token', "", expires=-1)
    return res
