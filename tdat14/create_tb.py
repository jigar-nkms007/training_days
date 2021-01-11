import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='jigar',passwd='jkljkl007',database='TEST')
mycursor=mydb.cursor()
mycursor.execute('show tables')

for tb in mycursor:
    print(tb)