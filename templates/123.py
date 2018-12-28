from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.126.com'

app.config['MAIL_PORT'] = 465

app.config['MAIL_USE_SSL'] = True

app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')

app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/')
def index():
    msg = Message(subject='你好', sender='jiejiekuawoshuai@126.com',
                  recipients=['jiejiekuawoshuai@126.com', 'jiejiekuawoshuai@163.com'])
    msg.body = '你好，这是来自flask-mail的一封邮件'
    msg.html = '<b>测试Flask 发送邮件</b>'
    mail.send(msg)

    return '邮件发送完成'
if __name__ == "__main__":
    app.run(debug=True)