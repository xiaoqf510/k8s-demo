import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 邮件发送配置
smtp_server = 'smtp.163.com'  # SMTP服务器地址
smtp_from = '18145536045@163.com'  # 发件人邮箱
smtp_auth_username = '18145536045@163.com'  # 邮箱用户名
smtp_auth_password = 'NCELIPSDQEAGLHLJ'  # 邮箱授权码
recipient_email = '3261593106@qq.com'  # 收件人邮箱

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
    subject = "代码部署到生产环境确认邮件"
    body = (
        "运维同事，您好，\n\n"
        "测试环境目前测试代码没问题，是否同意部署到生产环境？\n"
        "如果同意，请登录 Jenkins，将代码部署到生产环境。\n"
        "Jenkins 地址：http://192.168.40.180:30002/job/jenkins-harbor\n"
    )
    send_email(subject, body) 