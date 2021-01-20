import flask
from flask import request, jsonify
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='jigar',passwd='jkljkl007',database='TEST')
mycursor=mydb.cursor()

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'home page'

@app.route('/api/data/all')
def all_books():
    mycursor.execute('SELECT * FROM studentsdata')
    all_books = mycursor.fetchall()

    return jsonify(all_books)

@app.route('/api/data')
def filter():

    query= 'SELECT * FROM studentsdata WHERE'
    data_filter = []

    if 'rollno' in request.args:
        rollno= request.args['rollno']
        query=query+' rollno={} AND'.format(rollno)
        data_filter.append(rollno)
    if 'name' in request.args:
        name = request.args['name']
        query =query+ ' name={} AND'.format(name)
        data_filter.append(name)
    if 'marks' in request.args:
        marks = request.args['marks']
        query =query+ ' marks={} AND'.format(marks)
        data_filter.append(marks)

    query=query[:-4]


    mycursor.execute(query)

    result= mycursor.fetchall()

    return jsonify(result)

@app.route('/api/data/add',methods=['post'])
def add():
    json=request.json
    rollno= json['rollno']
    name=json['name']
    marks=json['marks']

    if rollno and name and marks and request.method=='POST':
        query= "INSERT INTO studentsdata (rollno,name,marks) values(%s,%s,%s)"
        data=[rollno,name,marks]
        mycursor.execute(query,data)
        mydb.commit()
    return 'data added'

@app.route('/api/data/update',methods=['PUT'])
def update():
    json=request.json
    rollno= json['rollno']
    name= json['name']
    marks=json['marks']

    if rollno and name and marks and request.method=='PUT':
        query = "update studentsdata set name=%s, marks=%s where rollno=%s "
        data= [name,marks,rollno]
        mycursor.execute(query,data)
        mydb.commit()

    return 'data update'

@app.route('/api/data/delete',methods=['DELETE'])
def delete():
    json=request.json
    rollno= json['rollno']

    if rollno and request.method=='DELETE':
        query = "delete from studentsdata where rollno=%s"
        data= [rollno]
        mycursor.execute(query,data)
        mydb.commit()
    return 'data deleted'

if __name__ == '__main__':
    app.run(debug=True)
