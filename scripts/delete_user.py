#!user/bin/python
# -*- coding: utf-8 -*-
import imaplib
import email
import email.header
from notification import *


def get_mailAction(status):
    #Here write the code for read eamil in IMAP
    mail = imaplib.IMAP4_SSL('imap.1and1.mx')
    mail.login(EmailUser,Password)
    mail.list()
    # Out: list of "folders" aka labels in gmail.
    mail.select("inbox") # connect to inbox.
    #(status, response) = mail.search(None, '(UNSEEN)')

    (t, data) = mail.search(None, status)
    mail_ids = data[0]

    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])


    #for i in range(latest_email_id,first_email_id, -1):
    #    print i
    #    typ, data = mail.fetch(i, '(RFC822)' )
    #    for response_part in data:
    #        if isinstance(response_part, tuple):
    #            msg = email.message_from_string(response_part[1])
    #            email_subject = msg['subject']
    #            print 'Subject : ' + email_subject + '\n'
    i = 0
    for value in id_list:
        i += 1
        typs, datas = mail.fetch(i, '(RFC822)' )
        for response_part in datas:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                email_subject = msg['subject']
                print 'Subject : ' + email_subject + '\n'

    mail.close()
    mail.logout()

def set_donw_sap():
    val = 0
    
    return val

###############################################################################
##                                                                           ##
##                                                                           ##
##                                  Main                                     ##
##                                                                           ##
###############################################################################

get_mailAction('ALL')
