from app.database.util import update, get, delete
from app.utils.auth.auth_util import get_login_user


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

    if coupon_type.get('count') <= 1:
        delete('coupon_type', {
            "id": coupon_type_id
        })
