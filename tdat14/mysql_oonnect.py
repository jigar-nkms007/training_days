import mysql.connector
mydb= mysql.connector.connect(host='localhost',user='jigar',passwd='jkljkl007')
print(mydb)

if (mydb):
    print('connection successfull')
else:
    print('unsucccessfull')