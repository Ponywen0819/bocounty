from flask import current_app
import smtplib
from dataclasses import dataclass
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from uuid import uuid4
import os


def send_verify_email(student_id: str, user_name: str):
    verify_code = uuid4().hex
    # get app setting
    setting: dict = current_app.config.get("setting")
    mail_setting: dict = setting.get("mail")
    host: str = mail_setting.get("host", "")
    port: int = mail_setting.get("port", 0)
    password: str = mail_setting.get("password", "")

    print(mail_setting)
    # initial email setting
    email = build_email(mail_setting, student_id, user_name, verify_code)
    with smtplib.SMTP(host="smtp.gmail.com", port=port) as smtp:  # 設定SMTP伺服器
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login(host, password)  # 登入寄件者gmail
        smtp.send_message(email)  # 寄送郵件


def build_email(setting: dict, student_id: str, user_name: str, code: str) -> MIMEMultipart:
    email = MIMEMultipart()
    email["subject"] = "Bocountry 驗證信件"
    email["from"] = "Bocountry@noreply.me"
    email["to"] = (setting.get("pattern") % student_id)

    email.attach(payload=build_html(user_name, code))
    return email


def build_html(user_name, code) -> MIMEText:
    file_name = "./static/email.html"
    html = ""
    with open(file_name, "r") as f:
        html = f.read()

    html = html.replace("{{ user_name }}", user_name)
    html = html.replace("{{ host }}", current_app.config["setting"]["host"])
    html = html.replace("{{ code }}", code)
    return MIMEText(html, 'html', 'utf-8')
