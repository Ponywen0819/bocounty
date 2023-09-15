from app.database.util import get_db
from app.database.formatter import get_keys_string, get_values_string
from uuid import uuid4


def create(table: str, value: dict):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(f"""
        INSERT INTO {table} 
        {get_keys_string(value)}
        VALUES {get_values_string(value)}
    """)

    db.commit()
