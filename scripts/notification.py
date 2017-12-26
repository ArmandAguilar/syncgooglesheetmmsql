#!user/bin/python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from tokensNotification import *

def send_notification(Subject,emailPerson,messages):
    val = ''
    try:
        msg = MIMEMultipart()
        msg['From'] = EmailUser
        msg['To'] = emailPerson
        msg['Subject'] = Subject
        message = messages
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP(Servidorsmtp,587)
        # identify ourselves to smtp gmail client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login(EmailUser, Password)
        mailserver.sendmail(EmailUser,emailPerson,msg.as_string())
        mailserver.quit()
        val = 'send email'
    except SMTPException:
        val = 'Error: unable to send email'
    return val

def talk_notification():
    val = 0
    return val

################################################################################
##                                                                            ##
##                                                                            ##
##                          Function Test                                     ##
##                                                                            ##
##                                                                            ##
################################################################################


#print(send_notification('Error MatrizHonorarios','a.aguilar@fortaingenieria.com','Mensaje de error aqui'))
