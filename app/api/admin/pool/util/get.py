from app.database.util import get
from .pool import Pool

def get_pool_list():
    pools = get('pool')

    return [Pool(**data) for data in pools]

