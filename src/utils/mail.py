from typing import Any
import smtplib

from email.mime.text import MIMEText


if __name__ == "__main__":
    import sys, os
    sys.path.insert(1, os.path.join(sys.path[0], "../.."))

from src.config import email_settings


class Mail:
    def __init__(self):
        self.sender = email_settings.LOGIN
        self.password = email_settings.PASS
        self.smtp_server = email_settings.SMTP
        self.smtp_server_port = email_settings.PORT

    def send(self, *, reciever: str, subject: str, text: Any):
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_server_port) as server:
            server.ehlo()
            server.login(self.sender, self.password)
            server.auth_login()
            msg = MIMEText(text)
            msg["From"] = self.sender
            msg["Subject"] = subject
            server.sendmail(self.sender, reciever, msg.as_string())


mail = Mail()