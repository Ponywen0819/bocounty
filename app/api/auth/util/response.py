from flask import Response
from datetime import datetime, timedelta
from app.utils.jwt_util import JWTGenerator


def with_jwt(res: Response, user: dict) -> Response:
    jwt_util = JWTGenerator()
    jwt_encode = jwt_util.generate_token({
        "id": user["id"]
    })
    res.set_cookie('user_token', jwt_encode, expires=datetime.now() + timedelta(days=2))

    return res


def without_jwt(res: Response) -> Response:
    res.set_cookie('user_token', "", expires=-1)
    return res
