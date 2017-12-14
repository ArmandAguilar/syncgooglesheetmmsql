#!user/bin/python
# -*- coding: Windows-1252 -*-
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
# -*- coding: IBM850 -*-
from credential import *



def update_cost():
    #here code !
    msj = 'Yupi!!!'
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
            if str(row[2])  > '0':
                #print ('%s   %s  %s' % (row[0],row[1],row[2]))
                costo = str(row[20]).replace(',','.')
                cadena = 'Id :' + str(row[2]) + ' Costo :' + str(costo)
                sql = 'UPDATE [SAP].[dbo].[RecursosCostos] SET [CostoUnitario] = \'' + str(costo) + '\' WHERE IdRecurso=\'' +  str(row[2]) + '\''
                print (str(sql))
#################################################################################
##                                                                             ##
##                              Test Function                                  ##
##                                                                             ##
#################################################################################

update_cost()
