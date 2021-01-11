import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='jigar',passwd='jkljkl007',database='TEST')
mycursor=mydb.cursor()
sql="update employee set salary = 50000 where name = 'jkl' "

mycursor.execute(sql)
mydb.commit()