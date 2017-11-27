#! /usr/bin/python
from __future__ import print_function
import httplib2
import os
import sys
import credentials
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

#from  credentials import get_credentials
import credentials

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'token.json'
APPLICATION_NAME = 'Sheets'

"""Shows basic usage of the Sheets API.

Creates a Sheets API service object and prints the names and majors of
students in a sample spreadsheet:
https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
"""
credentials = credentials.get_credentials()
http = credentials.authorize(httplib2.Http())
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
service = discovery.build('sheets', 'v4', http=http,discoveryServiceUrl=discoveryUrl)

spreadsheetId = '1pCQwLJUgBVa6Q-s35QpWn0lmO-s3k7sx2wFwZxQYPLs'
rangeName = ' Honorarios 2017!A7:F'
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheetId, range=rangeName).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        #print columns A and E, which correspond to indices 0 and 4.
        print('%s,%s,%s,%s,%s,%s' % (row[0],row[1],row[2],row[3],row[4],row[5]))
