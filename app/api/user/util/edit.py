from app.database.util import update


def edit_user(id: str, values: dict):
    update('account', {
        "id": id
    }, values)