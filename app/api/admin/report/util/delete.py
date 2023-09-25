from app.database.util import get, delete


def delete_request(request_id: str):
    request = get('request', {"id": request_id})[0]
    delete('order',{"id": request.get("order_id")})






