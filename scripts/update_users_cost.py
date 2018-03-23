#!user/bin/python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
# -*- coding: IBM850 -*-
#here section for tokes
from tokensDB import *
from credential import *
from tokensNotification import *
from notification import *
#here import connection to DB
import pypyodbc as pyodbc
import pymssql

def execute_SQL(sql,DB):
        valor = 'Procesando..'
        conn = pymssql.connect(host=hostMSSQL,user=userMSSQL,password=passMSSQL,database=DB)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        return sql

def update_cost():
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
                FechaSalida = str(row[23])
            except:
                FechaSalida = '1999-01-01'
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
            if str(costo)  > '0':
                #print ('%s   %s  %s' % (row[0],row[1],row[2]))
                if float(costo) > 0.0:
                    if str(iniciales) != '':
                        if str(depto) != '':
                            if str(perfil) != '':
                                if email !='':
                                    try:
                                        if int(row[2]) > 0:
                                            sqlCostos = 'UPDATE [SAP].[dbo].[RecursosCostos] SET [CostoUnitario] = \'' + str(costo) + '\' WHERE IdRecurso=\'' +  str(row[2]) + '\''
                                            sqlUser = 'UPDATE [Northwind].[dbo].[Usuarios] SET  FechaIngreso=\'' + str(FechaIngreso) + '\', FechaSalida=\'' + str(FechaSalida) + '\',Email=\'' + str(email) +  '\',Perfil=\'' + str(perfil) + '\',Acronimo=\'' + str(row[3]) + '\' WHERE Id=\'' + str(row[2]) + '\''
                                            #sqlUser = 'UPDATE [Northwind].[dbo].[Usuarios] SET  FechaIngreso=\'' + str(FechaIngreso) + '\', FechaSalida=\'' + str(FechaSalida) + '\',Email=\'' + str(email) + '\',Perfil=\'' + str(perfil) + '\',Acronimo=\'' + str(row[3]) + '\' WHERE Id=\'' + str(row[2]) + '\''
                                            execute_SQL(sqlCostos,'SAP')
                                            execute_SQL(sqlUser, 'Northwind')
                                            print (str(sqlCostos))
                                            print(str(sqlUser))
                                    except:
                                        send_notification('Error: MatrizHonorarios 2017','a.aguilar@fortaingenieria.com','Error: se pudo ejecutar la consulsa en el MMSQL Verificar el usuario (ID): ' + str(row[2]))

#################################################################################
##                                                                             ##
##                              Test Function                                  ##
##                                                                             ##
#################################################################################

update_cost()
