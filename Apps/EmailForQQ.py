# -*- coding: utf-8 -*-
"""
利用QQ邮箱给发送邮件
"""
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置SMTP服务器
mail_user="**********"   #SMTP服务器用户名,在这里填写QQ号
mail_pass="**********"   #SMTP服务器口令 
 
# 发送邮箱
sender = '**********@qq.com'  #QQ邮箱
# 接收邮件   
receivers = '**********@qq.com'  #QQ邮箱
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("Liuxi测试", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
try: 
    smtpObj = smtplib.SMTP_SSL(mail_host,465) 
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, [receivers,], message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except Exception:
    print("邮件无法发送")
#input()