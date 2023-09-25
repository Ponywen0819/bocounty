from app.database.util import delete


def delete_pool(pool_id: str):
    delete('pool', {
        "id": pool_id
    })
