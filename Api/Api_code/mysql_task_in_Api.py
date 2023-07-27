from flask import Flask, request, jsonify
import mysql.connector as conn

app =Flask(__name__)

mydb = conn.connect(host='localhost', user='root', passwd='Harekrishna@123')
cursor = mydb.cursor()
cursor.execute('create database if not exists myname')
cursor.execute('create table if not exists myname.mysqltable(name varchar(30), number int, emailid varchar(30), phone int(10)')


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into myname.mysqltable values(%s,%s)", (name, number))
        mydb.commit()
        return jsonify(str("succeesfully inserted"))

def update():
    if request.method=='POST':
        emailid =request.json['emailid']
        phone = request.json['phone']
        cursor.execute("insert into myname.mysqltable values(%s, %s)",(emailid, phone))
        mydb.commit()
        return jsonify(str("Successfully updated"))

if __name__ == '__main__':
    app.run()

