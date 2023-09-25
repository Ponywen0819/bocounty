from flask import request
from uuid import uuid4
from app.utils.auth.auth_util import get_login_user
from app.utils.time_util import get_current, date2str


def format_create_payload(id: str):
    payload: dict = request.json
    payload["id"] = uuid4().hex
    payload["order_id"] = id
    payload["publisher_id"] = get_login_user().get("id")
    payload["time"] = date2str(get_current())
