import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='jigar',passwd='jkljkl007',database='TEST')
mycursor=mydb.cursor()

mycursor.execute('select * from employee')

# result=mycursor.fetchone()

result= mycursor.fetchall()

for raw in result:
    print(raw)