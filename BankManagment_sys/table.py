import mysql.connector as sql

conn = sql.connect(host="localhost", user = "root", passwd = "ankit8ankit", database = 'bank')
if conn.is_connected():
    print("connected succesfully")
cur = conn.cursor()
cur.execute('create table customer_detail( acc_no int primary key , acc_name varchar(30), phone_no bigint(25) check(phone_no<11), address varchar(30), cr_amt float)')