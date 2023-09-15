from app.database.util import get

def get_order_list():
    orders = get('order')
    return


def get_order(id):
    orders = get('order', {})