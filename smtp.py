import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import argparse

# 邮件发送配置
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your_email@example.com"
SMTP_PASS = "your_email_password_or_auth_code"

def send_email(subject, body, receiver_email):
    try:
        message = MIMEMultipart()
        message['From'] = Header("Jenkins通知", 'utf-8')
        message['To'] = Header(receiver_email, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')

        message.attach(MIMEText(body, 'plain', 'utf-8'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, receiver_email, message.as_string())

        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败：{e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="发送邮件通知")
    parser.add_argument("--subject", required=True, help="邮件主题")
    parser.add_argument("--body", required=True, help="邮件正文")
    parser.add_argument("--to", required=True, help="收件人邮箱")

    args = parser.parse_args()
    send_email(args.subject, args.body, args.to)
