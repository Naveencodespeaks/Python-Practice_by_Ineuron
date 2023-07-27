import mysql.connector as conn
mydb = conn.connect(host="localhost", user="root", passwd="Harekrishna@123")
cursor = mydb.cursor()
#cursor.execute("create database Harekrishna")
#cursor.execute("show databases")
s = "create table Harekrishna.Harekrishnadetails3(employee_id int(10), emp_name varchar(80), emp_mailid varchar(50), emp_salary int(7), emp_attendence int(6))"
q1= cursor.execute(s)

q2 = cursor.execute("select *from Harekrishna.Harekrishnadetails3")
print(q2)


