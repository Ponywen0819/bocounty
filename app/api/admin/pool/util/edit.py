from app.database.util import update, get
from flask import request

from os import remove, getcwd, path


def edit_pool(pool_id: str):
    payload: dict = request.json

    pool = get('pool', {"id": pool_id})[0]

    file_url: str = pool.get('photo')

    file_name = file_url.split('/')[-1]

    file_path = path.join(getcwd(), 'public', file_name)

    remove(file_path)

    update('pool', {
        "id": pool_id
    }, payload)
