from app.utils.auth.auth_util import get_login_user
from app.utils.response import not_found
from app.database.util import get
from .response import no_enough_coin


def validate_buy(coupon_type_id):
    _validate_coupon_type_exist(coupon_type_id)
    _validate_coin(coupon_type_id)


def _validate_coupon_type_exist(coupon_type_id):
    coupon_types = get('coupon_type', {
        "id": coupon_type_id
    })

    if len(coupon_types) != 1:
        not_found('coupon type not found')


def _validate_coin(coupon_type_id: str):
    user = get_login_user()
    coin = user.get('bocoin')
    coupon_type = get('coupon_type', {
        "id": coupon_type_id
    })[0]

    if coin < coupon_type.get('price'):
        no_enough_coin()
