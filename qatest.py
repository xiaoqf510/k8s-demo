#作者微信->15011572657

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 邮件发送配置
smtp_server = 'smtp.163.com'  # SMTP服务器地址
smtp_from = '15573156063@163.com'  # 发件人邮箱
smtp_auth_username = '15573156063@163.com'  # 邮箱用户名
smtp_auth_password = 'QFjExRyXdUMCzTGR'  # 邮箱授权码
recipient_email = '483555203@qq.com'  # 收件人邮箱

def send_email(subject, body):
    try:
        # 创建邮件对象
        message = MIMEMultipart()
        message['From'] = Header(smtp_from, 'utf-8')
        message['To'] = Header(recipient_email, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文
        message.attach(MIMEText(body, 'plain', 'utf-8'))

        # 连接SMTP服务器并发送邮件
        with smtplib.SMTP(smtp_server, 25) as server:
            server.login(smtp_auth_username, smtp_auth_password)
            server.sendmail(smtp_from, recipient_email, message.as_string())

        print("邮件发送成功！")

    except Exception as e:
        print(f"邮件发送失败：{e}")

# 测试发送
if __name__ == "__main__":
    subject = "代码已发布到测试环境"
    body = (
        "各位好，\n\n"
        "代码已经成功发布到测试环境（qatest）。\n"
        "请访问以下路由，确认返回内容是否正常：\n"
        "http://192.168.40.180:31891\n\n"
        "如有问题请及时反馈！\n\n"
        "此致，\n测试团队"
    )
    send_email(subject, body)
