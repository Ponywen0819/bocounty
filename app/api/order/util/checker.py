from app.database.util import get_db
from app.utils.time_util import get_current,date2str

def check_order():
    cursor = get_db().cursor()

    cursor.execute(f"""
        DELETE FROM "order"
        WHERE exec_time < '{date2str(get_current())}' and exec_time != 'None'
    """)
