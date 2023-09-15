from app.database.util import delete


def delete_user(id: str):
    delete('account', {
        "id": id
    })
