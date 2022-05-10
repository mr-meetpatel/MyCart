'''

This File Manage connectivity to the database

'''
# import mysql connector which help to connect to mysql database
import mysql.connector
# import json which help to manage json data
import json

'''
1.Fetching Data From Config.json and store in params variable in json format
2.Config.json file has Database configuration.
'''

with open('config.json', 'r') as data:
    params = json.load(data)['params']

dbStatus = False
# Creating Object of database
try:

    mydb = mysql.connector.connect(
        host=params["host"],
        user=params["username"],
        password=params["password"],
        database=params["database"]
    )
    dbStatus = True
except:
    dbStatus = False


# Check if DB is connected or not
def is_connected():
    if dbStatus:
        return True
    else:
        return False





