import os

SECRET_KEY: bytes = "2cde2a0932ea7a1b3c3bdb621fddee2b211dedabfb5d090d6f8c5ea83eb064e2"
STORAGE_PATH: str = os.path.join(os.path.abspath("."), "storage")
SETTING_FILE: str = os.path.join(os.path.abspath("."), "setting.json")
DEBUG: bool = True
