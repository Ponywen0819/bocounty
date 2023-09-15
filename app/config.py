import os

SECRET_KEY: bytes = os.urandom(24)
STORAGE_PATH: str = os.path.join(os.path.abspath("."), "storage")
SETTING_FILE: str = os.path.join(os.path.abspath("."), "setting.json")
DEBUG: bool = True
