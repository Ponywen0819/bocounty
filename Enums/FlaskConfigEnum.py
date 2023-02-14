from enum import Enum


class FlaskConfigEnum(Enum):
    """
    有關 Flask 的 Config 儲存所使用的列舉
    """
    # AppConfig = 1
    # JWTGenerator = 2
    # Crypto = 3
    JWT_secret = 4
    SSL = 5
    SQL = 6
    Encrypt = 7
    UploadFolder = 8


