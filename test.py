from uuid import uuid4
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_verify_email():
    verify_code = uuid4().hex
    # get app setting
    host: str = "pony076152340@gmail.com"
    port: int = 587
    password: str = "hhsxfmasbyiovvty"

    # initial email setting
    email = build_email(verify_code)
    with smtplib.SMTP(host="smtp.gmail.com", port=port) as smtp:  # 設定SMTP伺服器
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login(host, password)  # 登入寄件者gmail
        smtp.send_message(email)  # 寄送郵件


def build_email(code: str) -> MIMEMultipart:
    email = MIMEMultipart()
    email["subject"] = "Bocountry 驗證信件"
    email["from"] = "Bocountry@noreply.me"
    email["to"] = "pony076152340@gmail.com"

    with open("./static/logo.png", "rb") as f:
        img_content = f.read()

    # mime_img = MIMEImage(img_content, name="logo.png")
    # mime_img.add_header("Content-ID", f"<{mime_img.get_filename()}>")
    # email.attach(mime_img)

    mime_html = build_html("pony", code)
    email.attach(mime_html)
    # email.set_payload(payload=build_html(user, code=code), charset="utf-8")
    # email.attach(mime_img)

    return email


def build_html(user, code) -> MIMEText:
    file_name = "./static/email.html"
    html = ""
    with open(file_name, "r") as f:
        html = f.read()

    html = html.replace("{{ user_name }}", user)
    html = html.replace("{{ host }}", "bocountry")
    html = html.replace("{{ code }}", code)
    return MIMEText(html, 'html', 'utf-8')


send_verify_email()
