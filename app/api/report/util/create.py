from flask import request
from app.database.util import create

def create_report():
    payload: dict = request.json
    create('report', payload)

