# Database : It is a collection of tables which contains lot of data
# importing pymysql module

import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")

mycursor = mydb.cursor()

# execute the query
mycursor.execute("create database IF NOT EXISTS 14march_python")

# save
mydb.commit()
print("Database Successfully Created!")

# db connection

mydb = pymysql.connect(host="localhost",user="root",password="",database="14march_python")
mycursor = mydb.cursor()

# table creation query executation

mycursor.execute("create table IF NOT EXISTS students(id int primary key auto_increment,name varchar(50),subject varchar(50))")
mydb.commit()
print("Table created successfully..")