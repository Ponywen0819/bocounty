from app.database.util import get_db
from app.database.formatter import get_condition_string


def get(table: str, condition: dict = None) -> list[dict]:
    column_names = get_column(table)

    cursor = get_db().cursor()
    query_string = f"SELECT * FROM '{table}' "

    if condition is not None:
        query_string += f"WHERE {get_condition_string(condition)}"

    select_query = cursor.execute(query_string)

    return [dict(zip(column_names, row)) for row in select_query]


def get_from_raw(table, string: str):
    column_names = get_column(table)

    cursor = get_db().cursor()

    select_query = cursor.execute(string)

    return [dict(zip(column_names, row)) for row in select_query]


def get_column(table: str) -> list:
    cursor = get_db().cursor()
    info_query = cursor.execute(f"""
            PRAGMA table_info('{table}')    
        """)

    column_names = [column_info[1] for column_info in info_query]
    return column_names
