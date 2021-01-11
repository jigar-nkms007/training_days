import mysql.connector
import random
import string
mydb = mysql.connector.connect(host='localhost',user='jigar',passwd='jkljkl007',database='TEST')
mycursor=mydb.cursor()
i=0
n = 10
z=5
a=[]
s=[]
r=[]
m=[]
im=[]

while(i<n):
    sid = random.randint(00000000, 99999999)
    rollno = random.randint(12000, 13000)
    marks = random.randint(300, 500)
    imarks = random.randint(50, 150)
    res = ''.join(random.choices(string.ascii_letters,k=z))
    s.append(sid)
    a.append(res)
    r.append(rollno)
    m.append(marks)
    im.append(imarks)
    i=i+1


student=[]

student1=[]
for i in range(0,n):
    student.append((r[i],a[i],m[i]))
    student1.append((s[i],r[i],im[i]))

# mycursor.execute('create table studentsdata (rollno int primary key,name varchar(10),marks int)')

sql="insert into studentsdata values(%s,%s,%s)"
mycursor.executemany(sql,student)

sql1="insert into studentsdata1 values(%s,%s,%s)"
mycursor.executemany(sql1,student1)

mydb.commit()