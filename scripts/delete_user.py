#!user/bin/python
# -*- coding: utf-8 -*-
import imaplib
import email
import email.header
from notification import *
#here section for tokes
from tokensDB import *
from tokensTW import *
from tokensNotification import *

#imports for jso and request
import json
import requests
from urllib2 import urlopen,base64
import unicodedata

def get_mailAction(status):
    val = 0
    #Here write the code for read eamil in IMAP
    mail = imaplib.IMAP4_SSL(Servidorimap)
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
                #print 'Subject : ' + email_subject + '\n'
                txtEmailUser = str(email_subject).split(' ')
    mail.close()
    mail.logout()
    if txtEmailUser[0] == 'Delete' or txtEmailUser[0] == 'Borrar':
        #print('Delete: ' + txtEmailUser[1])
    else:
        val = 0
    return val
def set_donw_sap():
    val = 0

    return val

def set_down_teamwork(email):
    val = 0
    #Here we create the data in Json
    data = {'person':{}}
    data['person']['password'] = 'rashidMX01**'
    dataJson = json.dumps(data)
    #Here make the validate for create
    r = requests.get(url + '/people.json?emailaddress=' + str(email) , auth = (key, ''))
    data = json.loads(r.text,encoding='utf-8',cls=None,object_hook=None, parse_float=None,parse_int=None, parse_constant=None,object_pairs_hook=None)
    if len(data['people']) > 0:
        Id = data['people'][0]['id']
        val =  Id
        #Here change the password of user
        urlPut =    url + '/people/' + str(Id) + '.json'
        requestUser  = requests.put(urlPut ,auth = (key, ''), data=dataJson)
        print (urlPut)
    else:
        val = 0
    return val

def set_down_pipesrive():
    val = 0

    return val


###############################################################################
##                                                                           ##
##                                                                           ##
##                                  Main                                     ##
##                                                                           ##
###############################################################################

get_mailAction('ALL')
#print set_down_teamwork('a.aguilar@fortaingenieria.com')
