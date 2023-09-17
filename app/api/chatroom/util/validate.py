from app.database.util import get, get_db
from app.utils.response import not_found
from .response import already_exist
from app.utils.auth.auth_util import get_login_user


def validate_create_payload(id):
    _validate_create_order(id)
    _validate_conflict(id)

def _validate_conflict(id):
    user = get_login_user()

    cursor = get_db().cursor()
    cursor.execute(f"""
        SELECT * FROM chatroom, chatroom_member
        WHERE 
            chatroom.id = chatroom_member.chatroom_id AND 
            chatroom_member.account_id = '{user.get('id')}' AND
            chatroom.order_id = '{id}'
    """)

    chatroom_list = cursor.fetchall()

    print(chatroom_list)
    if len(chatroom_list) != 0:
        already_exist()

def _validate_create_order(id):
    orders = get('order', {
        "id": id
    })

    if len(orders) != 1:
        not_found('order not found')


