import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender='120833@qq.com'  # 邮箱
my_pass = ''    # 申请的密码，不是QQ密码
my_user='120833@qq.com'  # 接收人[可以是自己]
def mail():
    try:
        msg=MIMEText('iPhone12有货了，抓紧订购！！','plain','utf-8')
        msg['From'] = formataddr(["BIAO",my_sender])
        msg['To'] = formataddr(["标",my_user])
        msg['Subject'] = "iPhone12预约提醒"

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender,[my_user,],msg.as_string())
        server.quit()
    except Exception:
        print('邮件发送异常')

while True:
  url ='https://reserve-prime.apple.com/CN/zh_CN/reserve/F/availability.json'

  res = requests.get(url).json()

  flag = res.get('stores').get('R531').get('MGH53CH/A').get('availability').get('contract')

  if flag:
    mail()
    break
  time.sleep(10)