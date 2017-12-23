#!user/bin/python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
# -*- coding: IBM850 -*-
#import for google apis
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

#imports for jso and request
import json
import requests
from urllib2 import urlopen,base64
#here section for tokes
from tokensDB import *
from tokensTW import *
#here import connection to DB
import pypyodbc as pyodbc
import pymssql
#Here import the function by make login in google apis
from credential import *


#this function get the last id in the table user of Northind
def lastId():
    ID = 0
    sql = 'SELECT [Id] FROM [Northwind].[dbo].[Usuarios] order by Id asc'
    con = pyodbc.connect(constrNorthwind)
    cur = con.cursor()
    cur.execute(sql)
    for value in cur:
        ID = value[0]
    con.commit()
    con.close()
    return ID + 1
#this function create a new user en teamwork and get your ID
def createUserTemwork(firstName,lastName,email,userName,password):
    Id = 0
    company = "https://forta"
    key = "dublin527patrick"
    url = "https://forta.teamwork.com"
    data = {'person':{}}
    data['person']['first-name'] = firstName
    data['person']['last-name'] = lastName
    data['person']['email-address'] = email
    data['person']['user-type'] = 'account'
    data['person']['user-name'] = firstName
    data['person']['password'] = password
    data['person']['company-id'] = '98191'


    dataJson = json.dumps(data)
    print (str(dataJson))
    #r = requests.post(url + '/people.json' ,auth = (key, ''), data=dataJson)
    #data = json.loads(r.text,encoding='utf-8',cls=None,object_hook=None, parse_float=None,parse_int=None, parse_constant=None,object_pairs_hook=None)
    #Print Staus Code to know that happed , in production c¡be comment
    #print(r.status_code)
    #print(r.text)
    #print(r.json)
    #{u'STATUS': u'OK', u'id': u'317825'}
    #Id = r.json()['id']
    #return Id

def instertRecurso(id,nombre,costo):
    sql = 'INSERT INTO [SAP].[dbo].[RecursosCostos] VALUES (\'' + str(nombre) + '\',\'' + str(id) + '\',\'' + str(costo) + '\')'

    return sql
def execute_SQL(sql,DB):
        valor = 'Procesando..'
        conn = pymssql.connect(host=hostMSSQL,user=userMSSQL,password=passMSSQL,database=DB)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        return sql
def create_user():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    service = discovery.build('sheets', 'v4', http=http,discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '17cWeLtwVbadMM0MZlwXoovif3hJQV4skXMwNlXQwUvo'
    spreadsheetId = '1pCQwLJUgBVa6Q-s35QpWn0lmO-s3k7sx2wFwZxQYPLs'
    rangeName = 'Honorarios2017!A7:W'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            #print columns A and E, which correspond to indices 0 and 4.
            #Search the values empyts
            if str(row[2])  == '0':
                #Here apply the filtre by errors in the sheets)
                #Here we filter the INICIALES

                if str(row[3]) == '':
                    #Send notification
                    v = 0
                    print ('Faltan Iniciales')
                #Here we filter Depto
                elif str(row[4]) == '':
                    #Send notification
                    v = 0
                    print ('Faltan Departamento')
                #Here we filter Puesto
                elif str(row[5]) == '':
                    #Send notification
                    v = 0
                    print ('Faltan Pueto')
                #Here filter email
                elif str(row[6]) == '':
                    #send notification
                    v = 0
                    print ('Faltan Email')
                #Here filter Costo
                elif str(row[20]) == '':
                    #send notification
                    v = 0
                    print ('Faltan Costo')
                #Here fecha
                elif str(row[22]) == '':
                    #send notification
                    v = 0
                    print ('Faltan Fecha')
                else:
                    #Registre the new user
                    try:
                        pass
                        IdUser = lastId()
                        costo = str(row[20]).replace(',','.')
                        pwd = 'fortaMX' + str(IdUser) + '**'
                        IdUserTeamWork =  createUserTemwork(str(row[0].strip()),str(row[1].strip()),str(row[6]),str(row[0]),str(pwd))
                        nombre = str(row[0].encode("iso-8859-1"))
                        apellidos = str(row[1].encode("iso-8859-1"))
                        depto = str(row[4].encode("iso-8859-1"))
                        perfil = str(row[5].encode("iso-8859-1"))
                        Sql = 'INSERT INTO [Northwind].[dbo].[Usuarios] VALUES (\'' + str(IdUser) + '\',\'0\',\'' + str(nombre.strip()) + '\',\'' + str(apellidos.strip()) + '\',\'Usuario\',\'' + str(row[6].strip()) + '\',\'' + str(pwd) + '\',\'' + str(depto.strip()) + '\',\'' + str(perfil.strip()) + '\',\'.\',\'0\' ,\'' + str(row[3].strip()) + '\',\'\',\'\' ,\'Si\',\'' + str() + '\',\'' + str(row[22]) + '\')'
                        SqlRecursos = instertRecurso(IdUser,row[0],costo)
                        print(Sql)
                        #execute_SQL(Sql,dbMSSQLNorthwind)
                        print(SqlRecursos)
                        #execute_SQL(SqlRecursos,dbMSSQLSAP)
                    except Exception as e:
                        raise


#################################################################################
##                                                                             ##
##                              Test Function                                  ##
##                                                                             ##
#################################################################################

create_user()
