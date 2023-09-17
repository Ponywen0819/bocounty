from app.database.util import delete

def delete_order(order_id: str):
    delete('order', {
        "id": order_id
    })