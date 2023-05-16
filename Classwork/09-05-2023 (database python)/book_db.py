# importing modules

import book_connection
import pymysql

# connect with database
mybook = pymysql.connect(host="localhost",user="root",password="",database="practice11")
mycursor = mybook.cursor()

status = True
while  status:
    menu="""
            1) insert data
            2) view data
            3) Update data
            4) Search data
            5) Delete data
    
    """
    print(menu)
    choice = int(input("Enter Your Choice : "))
    
    if choice == 1:
        # to insert data
        name = input("Enter Book Name : ")
        isbn = int(input("Enter ISBN NO. : "))
        price = input("Enter Price : ") 
        
        # query 
        query = "insert into mybooks (name,ISBN_NO,price) values ('%s',%s,'%s')"
        
        args = (name,isbn,price)
        
        mycursor.execute(query % args)
        
        # to save the changes
        mybook.commit()
        
        print("Book Data Added")
    
    elif choice == 2:

        # to view data
        mycursor.execute("select * from mybooks")
        
        mybook.commit()
        
        data = mycursor.fetchall()
        print(data)
        
        
    elif choice == 3:
        
        # update data
        
        id = int(input("Enter ID : "))
    
        name = input("Enter Book name : ")
        isbn = int(input("Enter ISBN No. : "))
        price = input("Enter Price : ")
        
        # query 
        query = "update mybooks set name = '%s',ISBN_NO = %s,price = '%s' where id = %s"
        
        args = (name,isbn,price,id)
        
        mycursor.execute(query % args)
        mybook.commit()
        
        print("Data Succesfully updated...")
        
    
    elif choice == 4:
        #search data
        id = int(input("Enter ID : "))
        
        # query 
        query = "select * from mybooks where id = %s"
        
        # args 
        args = (id)
        
        mycursor.execute(query % args)
        
        # display all data in row variable
        
        row = mycursor.fetchone()

        # id = 0 name = 1 isbn = 2 price = 3
        displayName = row[1]
        displayIsbn = row[2]
        displayPrice = row[3]
        
        print("Name = ",displayName)
        print("ISBN No. = ",displayIsbn)
        print("Price = ",displayPrice) 
        
        mybook.commit()  
        
    elif choice == 5:
        # delete data
        
        id = int(input("Enter ID : "))
        
        
        # query 
        query = "delete from mybooks where id  = %s"
        
        # args
        args = (id)
        
        mycursor.execute(query % args)
        
        mybook.commit()
        
        print("Data Deleted Successfully....")
        
    loop_choice = input("Want perform more op ? y/n :")
    if loop_choice == "n" or loop_choice == "N":
            status = False
            print("Thank you for using our database!")