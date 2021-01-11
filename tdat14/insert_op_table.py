import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='jigar',passwd='jkljkl007',database='TEST')
mycursor=mydb.cursor()

sqlq='insert into employee(name,salary) values(%s,%s)'

employees = [('jkl',40000),('xyz',30000),('xcv',20000)]
mycursor.executemany(sqlq,employees)

mydb.commit()

