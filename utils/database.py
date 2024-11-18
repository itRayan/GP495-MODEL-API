import pymysql.cursors
import re

connection = None

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        database='DATABASE',
        cursorclass=pymysql.cursors.DictCursor
    )
except pymysql.Error as err:
    raise Exception(err)

def extractSchema():
    if(connection):
        try:
            connection.ping(reconnect=True)
            cursor = connection.cursor()
            cursor.execute('SHOW TABLES;')
            
            tables = cursor.fetchall()

            schema = []

            for table in tables:
                table = list(table.values())[0] # Get table name
                cursor.execute('SHOW CREATE TABLE ' + table)
                result = cursor.fetchone()['Create Table']
                
                schema.append(re.sub(r" ENGINE.*", "", result))
            
            return schema
        except pymysql.Error as err:
            raise Exception(err)