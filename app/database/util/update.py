from app.database.util import get_db
from app.database.formatter import get_condition_string, get_setter_string


def update(table: str, condition: dict, value: dict):
    db = get_db()
    cursor = db.cursor()
    query_string = f"UPDATE '{table}' "

    if value is not None:
        query_string += f"SET {get_setter_string(value)} "

    if condition is not None:
        query_string += f"WHERE {get_condition_string(condition)} "

    cursor.execute(query_string)
