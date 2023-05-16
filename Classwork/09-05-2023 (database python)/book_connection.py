# import pymysql module  
import pymysql

mybook = pymysql.connect(host="localhost",user="root",password="")
mycursor = mybook.cursor()

# execute the query
mycursor.execute("create database IF NOT EXISTS practice11")

# save
mybook.commit()
print("Database is Succesfully created...")

# db connection
mybook = pymysql.connect(host="localhost",user="root",password="",database="practice11")
mycursor = mybook.cursor()

# table creation 
mycursor.execute("create table IF NOT EXISTS mybooks(id int primary key auto_increment,name varchar(50),ISBN_NO int,price varchar(50))")
mybook.commit()
print("Table Created Successfully.....")