import jwt
from flask import Config
from Enums.FlaskConfigEnum import FlaskConfigEnum as ConfigEnum


class JWTGenerator:
    def __init__(self, config: Config) -> None:
        self.secret_key = config[ConfigEnum.JWT_secret]

    def generate_token(self, values: dict) -> str:
        return jwt.encode(values, self.secret_key, algorithm='HS256')

    def check_token_valid(self, token: str) -> bool:
        try:
            data = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return True
        except:
            return False

    def get_token_detail(self, token: str) -> dict:
        return jwt.decode(token, self.secret_key, algorithms=['HS256'])