from app.database.util import get_db
from app.database.util.get import get_column

PAGESIZE = 20


def get_notification_with_page(page: int):
    column_names = get_column("notification")

    page -= 1

    cursor = get_db().cursor()
    select_query = cursor.execute(f"""
        SELECT * FROM notification
        ORDER BY timestamp DESC 
        LIMIT {PAGESIZE} OFFSET {page * PAGESIZE}
    """)

    return [dict(zip(column_names, row)) for row in select_query]
