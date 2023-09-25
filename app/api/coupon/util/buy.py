from app.database.util import update, get, delete, create
from app.utils.auth.auth_util import get_login_user
from app.database.model.coupon import create_coupon

def buy(coupon_type_id: str):
    user = get_login_user()
    coupon_type = get('coupon_type', {
        "id": coupon_type_id
    })[0]
    update('account', {
        "id": user.get('id')
    }, {
               "bocoin": user.get('bocoin') - coupon_type.get('price')
           })

    update('coupon_type', {
        "id": coupon_type_id
    }, {
               "count": coupon_type.get('count') - 1
           })

    create_coupon(user.get('id'), coupon_type_id)
