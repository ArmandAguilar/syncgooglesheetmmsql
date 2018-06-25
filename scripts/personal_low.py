#!user/bin/python
# -*- coding: utf-8 -*-
#here section for tokes
from tokensDB import *
from credential import *
from tokensNotification import *
from notification import *
#here import connection to DB
import pypyodbc as pyodbc
import pymssql

def execute_SQL(sql, DB):
    valor = 'Procesando..'
    conn = pymssql.connect(host=hostMSSQL, user=userMSSQL, password=passMSSQL, database=DB)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return sql

def update_status():
    #here code !
    msj = 'Yupi!!!'
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    service = discovery.build('sheets', 'v4', http=http,discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '17cWeLtwVbadMM0MZlwXoovif3hJQV4skXMwNlXQwUvo'
    spreadsheetId = '1pCQwLJUgBVa6Q-s35QpWn0lmO-s3k7sx2wFwZxQYPLs'
    rangeName = 'Honorarios2018!A7:X'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            #Here do a validate of data
            FechaSalida = '1999-01-01'
            FechaIngreso = '1999-01-01'
            try:
                FechaIngreso = str(row[22])
            except:
                FechaIngresos = '1999-01-01'
            try:
                SFecha = str(row[23]).split("-")
                FechaSalida = SFecha[2] + '-' + SFecha[1] + '-' + SFecha[0]
            except:
                FechaSalida = '01-01-1999'
            try:
                email = str(row[6].encode("iso-8859-1"))
            except:
                email = ''
            try:
                depto = str(row[4].encode("iso-8859-1"))
            except:
                depto = ''
            try:
                perfil = str(row[5].encode("iso-8859-1"))
            except:
                perfil = ''
            try:
                iniciales = str(row[5].encode("iso-8859-1"))
            except:
                iniciales = ''
            try:
                costo = str(row[20]).replace(',', '.')
            except:
                costo = 0
                #print columns A and E, which correspond to indices 0 and 4.
            #Search the values empyts
            if int(row[2]) > 0:
                try:
                    if str(row[21]) == 'INACTIVO':
                        sql = 'UPDATE [Northwind].[dbo].[Usuarios] SET [Departamento] = \'Baja\' ,[FechaSalida] = \'' + str(FechaSalida) + '\' WHERE Id=\'' + str(row[2]) + '\''
                        print(sql)
                        execute_SQL(sql,'Northwind')
                except:
                    vars = ''
#################################################################################
##                                                                             ##
##                              Test Function                                  ##
##                                                                             ##
#################################################################################

update_status()