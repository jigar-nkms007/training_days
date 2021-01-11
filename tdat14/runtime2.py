import mysql.connector
import random
import string
mydb = mysql.connector.connect(host='localhost',user='jigar',passwd='jkljkl007',database='TEST')
mycursor=mydb.cursor()
sql= 'select s.rollno,s1.sid,s.name,s.marks,s1.internalmarks from studentsdata as s , studentsdata1 as s1 WHERE s.rollno = s1.rollno'
mycursor.execute(sql)
result=mycursor.fetchall()
for raw in result:
    print(raw)
mydb.commit()