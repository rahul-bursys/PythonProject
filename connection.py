import mysql.connector

cnx = mysql.connector.connect(user='test', password='test1234',
                              host='127.0.0.1',
                              database='user')
cnx.close()
