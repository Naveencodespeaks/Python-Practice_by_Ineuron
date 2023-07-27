import mysql.connector as conn
mydb = conn.connect(host="localhost", user="root", passwd="Harekrishna@123")
cursor = mydb.cursor()
s = "insert into Harekrishna.Harekrishnadetails2 values(102, 'Hare', 'Hare@gmail.com', 1000000, 31)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)

mydb.commit()

cursor.execute("select * from Harekrishna.Harekrishnadetails2")
for i in cursor.fetchall():
    print(i)
