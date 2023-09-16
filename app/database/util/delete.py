from app.database.util import get_db
from app.database.formatter import get_condition_string


def delete(table: str, condition: dict):
    db = get_db()
    cursor = db.cursor()

    query_string = f"DELETE FROM {table} "

    if condition is not None:
        query_string += f"WHERE {get_condition_string(condition)} "

    cursor.execute(query_string)
