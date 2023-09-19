from app.database.util import update, get
from app.utils.time_util import get_current, date2str
from app.utils.auth.auth_util import get_login_user
from .chatroom import ChatroomStatus, OrderStatus

def confirm_chatroom(chatroom_id: str):
    chatroom = get("chatroom", {"id": chatroom_id})[0]
    order = get('order', {"id": chatroom.get('order_id')})[0]

    update('chatroom', {
        "id": chatroom_id
    }, {
               "status": ChatroomStatus.CONFIRM.value
           })

    exc_time = date2str(get_current()) if order.get('exc_time') == "None" else order.get('exc_time')
    update('order', {
        "id": order.get('id')
    }, {
               "status": OrderStatus.COMPLETED.value
           })

    undertaker_id = get_other_member(chatroom_id)
    undertaker = get('account', {"id": undertaker_id})[0]

    update('account',{
        "id": undertaker.get('id')
    },{
        "bocoin" : undertaker.get('bocoin') + order.get('price')
    })

def get_other_member(chatroom_id: str):
    chatroom_members = get('chatroom_member', {"chatroom_id": chatroom_id})
    user = get_login_user()

    for chatroom_member in chatroom_members:
        member_id = chatroom_member.get('account_id')
        if member_id != user.get('id'):
            return member_id
