# Teamwork To MMSQL

> This script read the Matriz-Honorarios-2017 (Google Sheets) and proceses the new user, when the field Id is 0 the script know the user is new in the system ,read all row and register a new user in SAP (MMSQL) and Teamwork.

### Tools used in this project

- Python 2.7.11
- pypyodbc
- urllib2
- json
- unicodedata
- datetime,time
- httplib2
- os
- apiclient
- oauth2client
- requests

### Descriptions of scripts

**mian.py** : In this script are all function that can create user or update user.

**credential.py** : The script have all tools that we needs to do login with the Api’s google sheet v4. 

**create_user.py** : With this script can read the Sheets of google (MatrizHonorarios2017) and create new user in SAP and Teamwork.
 
**update_user.py** :  With this script we can update the cost in our system’s cost the table sap.RecurosCostos. 

**notification.py** : This script send a email when happen a error in others scripts.

**TokenTW.py** : This  script have the user and tokens var for TeamworAPI.

**TokenDB.py** : This script have the connectionString, user and password to connect to MSSQL.

![How is works](https://github.com/ArmandAguilar/syncgooglesheetmmsql/blob/master/graffle/How%20is%20work.png)
