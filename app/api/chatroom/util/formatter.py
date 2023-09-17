from uuid import uuid4


def format_create_payload(order_id: str):
    payload: dict = dict()

    payload['id'] = uuid4().hex
    payload['order_id'] = order_id

    return payload