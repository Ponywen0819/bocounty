import base64
import os
import uuid

from flask import current_app
from enum import Enum
import re


class StorgeCode(Enum):
    POOL = 'pool'
    ITEM = 'item'


def storage_photo(raw_data: str, code: StorgeCode) -> str | None:
    split = re.split(r'[,;]\s*', raw_data)
    if len(split) != 3:
        return None
    data_type, encode_form, data = split

    if encode_form != 'base64':
        return None
    elif not re.match('^data:image/*', data_type):
        return None
    else:
        file_type = data_type[11:]
        print(file_type)
        photo_name = '%s.%s' % (uuid.uuid4().hex, file_type)
        decode_data = base64.b64decode(data)
        storage_write_bytes(photo_name, decode_data, code)
        return "/storage/%s/%s" % (code.value, photo_name)


def storage_write_bytes(filename: str, data: bytes, code: StorgeCode) -> None:
    file_path = os.path.join(current_app.config['STORAGE_PATH'], code.value, filename)
    print(os.getcwd(), file_path)
    with open(file_path, 'wb') as f:
        f.write(data)


def storage_write(filename: str, data: str, code: StorgeCode) -> None:
    file_path = os.path.join(current_app.config['STORAGE_PATH'], code.value, filename)
    with open(file_path, 'w') as f:
        f.write(data)




