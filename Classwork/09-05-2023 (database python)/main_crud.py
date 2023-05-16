# importing connection and pymysql

import connection
import pymysql

# connect with database
mydb = pymysql.connect(host="localhost",user="root",password="",database="14march_python")

mycursor = mydb.cursor()

status = True
while status:
    menu  = """
                1) Insert data
                2) View data
                3) Update data
                4) Search data
                5) Delete data
    
    """
    print(menu)
    
    choice = int(input("Enter Your Choice : "))
    
    if choice==1:
        # to insert data
        name = input("Enter Your Name : ")
        subject = input("Enter Your Subject : ")
        
        # query
        query = "insert into students (name, subject) values ('%s','%s')"
        
        args = (name,subject)
        
        mycursor.execute(query % args)
        
        # to save changes 
        mydb.commit()
        print("Data Successfully Inserted ")
        
    elif choice == 2:
        # to fetch all data from the table
        query = "select * from students"
        
        # to execute query
        mycursor.execute(query)
        mydb.commit()
        
        # to fetch data from table
        data = mycursor.fetchall()
        print(data)    
    
    elif choice == 3 :
        # update data
        id = int(input("Enter ID : "))
        name = input("Enter Name : ")
        subject = input("Enter Subject : ")
        
        # query
        query = "update students set name = '%s',subject = '%s' where id = %s"
        args = (name,subject,id)
        
        mycursor.execute(query % args) 
        mydb.commit()
        print("Data Updated Succesfully...")
    
    elif choice == 4 : 
        # search data
        
        id = int(input("Enter ID : "))
        
        # query 
        query = "select * from students where id=%s"
        
        # args 
        args = (id)
        
        mycursor.execute(query % args)
        
        # display all data in row variable 
        row = mycursor.fetchone()
        
        # id = 0 name = 1 subject = 2
        
        displayName = row[1]
        displaySubject = row[2]
        
        # print
        print("name = ",displayName)
        print("subject = ",displaySubject)
        
        mydb.commit()
        
        
    elif choice == 5:
        
        # delete data
        id = int(input("Enter ID : "))
        
        # query 
        query = "delete from students where id = %s"
        
        # args
        args = (id)
        
        mycursor.execute(query % args)
        
        mydb.commit()
        
        print("Data Deleted Successfully....")
        
            
    loop_choice = input("Want perform more op ? y/n :")
    if loop_choice == "n" or loop_choice == "N":
            status = False
            print("Thank you for using our database!")