# 配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑
import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:
    def __init__(self, username, passwd, recv, title, content, file=None, ssl=False, email_host='smtp.163.com', port=25, ssl_port=465):
        self.username = username  # 用户名
        self.passwd = passwd  # 密码
        self.recv = recv  # 收件人  多个收件人用list,如["1@qq.com", "2@qq.com"]
        self.title = title  # 邮件标题
        self.content = content  # 邮件正文
        self.file = file  # 附件路径
        self.email_host = email_host  # smtp服务器地址
        self.port = port  # 普通端口
        self.ssl = ssl  # 是否安全链接
        self.ssl_port = ssl_port  # 安全链接端口

    def send_email(self):
        msg = MIMEMultipart()
        if self.file:
            file_name = os.path.split(self.file)[-1]
            try:
                f = open(self.file, 'rb').read()
            except Exception as ex:
                raise Exception('附件打不开！！！')
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                att["Content-Disposition"] = 'attachment; filename="%s"' % new_file_name
                msg.attach(att)
        msg.attach(MIMEText(self.content))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送人
        msg['To'] = ','.join(self.recv)  # 收件人
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print('出错了。。。', e)
        else:
            print('发送成功！')
        self.smtp.quit()


if __name__ == "__main__":
    m = SendEmail(
        username='yfj15288451258@163.com',
        passwd='JHEOYJSLFOIZXVJG',
        recv=['1028306133@qq.com'],
        title='ceshi',
        content='测试发送邮件',
        file='D:/Users/10283/PycharmProjects/APItest/result/report.html',
        ssl=True,
    )
    m.send_email()
