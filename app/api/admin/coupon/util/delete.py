from app.database.util import delete


def delete_coupon(coupon_id: str):
    delete('coupon_type',{
        "id": coupon_id
    })