from app.database.util import get, update, delete, get_db


def assign_order(chatroom_id: str):
    chatroom = get('chatroom', {
        "id": chatroom_id
    })[0]

    update('order', {
        "id": chatroom.get('order_id')
    }, {
               "status": 1
           })

    cursor = get_db().cursor()

    cursor.execute(f"""
        DELETE FROM 'chatroom'
        WHERE id != '{chatroom_id}' AND order_id = '{chatroom.get('order_id')}'
    """)
