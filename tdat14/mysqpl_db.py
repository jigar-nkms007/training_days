import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='jigar',passwd='jkljkl007')
mycursor = mydb.cursor()
mycursor.execute('show databases')

for db in mycursor:
    print(db)