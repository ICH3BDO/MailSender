# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from colored import fg, bg, attr

srv_login_usr = input('[>>>] Put Your SMTP Login Mail :')
srv_login_pas = input('[>>>] Put Your SMTP Login Pass :')
print("="*25)
mail_list = input('[>>>] Put List Here : ')
your_mail = input('[>>>] Put Your Mail : ')
load_letr = input('[>>>] Put Letter Code :')
slct_mthd = input('[>>>] Text Or HTML Code [T/H] : ').capitalize()
print("="*25)
server = input('[>>>] Put SMTP Server : ')
srport = int(input('[>>>] Put SMPT Port : '))
print("="*25)
sub = input('[>>>] Put Your Subject : ')

mails = open(mail_list, 'r')

if slct_mthd == "T":
    for mail in mails:
        me = your_mail
        you = mail
        leter = open(load_letr, 'r', encoding="UTF-8").read()
        msg = MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = you
        text = str(leter)
        msg.attach(MIMEText(text, 'plain'))
        s = smtplib.SMTP(server, int(srport))
        s.ehlo()
        s.starttls()
        s.login(srv_login_usr, srv_login_pas)
        try:
            s.sendmail(me, you, msg.as_string())
            print(f'Message Sent To {mail} Successfully')
        except:
            print(f'Message Unsent To {mail}')
        s.quit()


elif slct_mthd == "H":
    for mail in mails:
        me = your_mail
        you = mail
        leter = open(load_letr, 'r', encoding="UTF-8").read()
        msg = MIMEMultipart('alternative')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = you
        html = str(leter)
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        s = smtplib.SMTP(server, int(srport))
        s.ehlo()
        s.starttls()
        s.login(srv_login_usr, srv_login_pas)
        try:
            s.sendmail(me, you, msg.as_string())
            print(f'Message Sent To {mail} Successfully')
        except:
            print(f'Message Unsent To {mail}')
        s.quit()

else:
    print("")
