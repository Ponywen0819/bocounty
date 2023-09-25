from app.database.util import get
from .order import Order
from app.database.util import get_from_raw
from app.database.model.order import OrderStatus
from app.utils.auth.auth_util import get_login_user


def get_order_list():
    orders = get('order')
    return [Order(**order) for order in orders]


def get_open_order():
    user = get_login_user()

    orders = get_from_raw('order', f"""
        SELECT * FROM 'order'
        WHERE status = {OrderStatus.RECRUITING.value} AND owner_id != '{user.get('id')}'
    """)

    return [Order(**order) for order in orders]


def get_enrolled_order():
    user = get_login_user()
    orders = get('order_enrolled', {
        "account_id": user.get('id')
    })

    return [Order(
        id=data['id'],
        status=data['status'],
        title=data['title'],
        intro=data['intro'],
        price=data['price'],
        owner_id=data['owner_id'],
        start_time=data['start_time'],
        close_time=data['close_time'],
        exec_time=data['exec_time']) for data in orders]


def get_order(order_id: str):
    order = get('order', {
        "id": order_id
    })[0]

    return Order(**order)
