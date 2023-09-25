from app.utils.auth.auth_util import get_login_user
from app.database.util import get_db
from app.database.util.get import get_column

PAGESIZE = 20


def get_notification_with_page(page: int):
    user = get_login_user()
    column_names = get_column("notification")

    page -= 1

    cursor = get_db().cursor()
    select_query = cursor.execute(f"""
        SELECT * FROM notification
        WHERE receiver_id = '{user.get('id')}'
        ORDER BY timestamp DESC 
        LIMIT {PAGESIZE} OFFSET {page * PAGESIZE}
    """ )

    return [dict(zip(column_names, row)) for row in select_query]
