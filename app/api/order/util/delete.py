from app.database.util import delete, get
from .validate import validate_permission


def delete_order(id: str):
    validate_permission(id)
    delete('order', {
        "id": id
    })