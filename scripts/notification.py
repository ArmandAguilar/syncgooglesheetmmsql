#!user/bin/python
import smtplib


def send_notification():
    val = 0
    fromaddr = 'ventas@fortaingenieria.com'
    toaddrs  = 'a.aguilar@fortaingenieria.com'
    msg = 'Why,Oh why!'
    username = 'notification_ia@fortaingenieria.mx'
    password = 'fortaMX010203*'
    server = smtplib.SMTP('smtp.1and1.mx:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
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


send_notification()
