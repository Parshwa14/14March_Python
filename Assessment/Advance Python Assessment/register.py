# importing all the tkinter module
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


# create a screen 
scr = Tk()

# create a title
scr.title("Registration Form")

# screen size
scr.geometry("400x550")

# locking the windows size
scr.resizable(0,0)

def sbmt():
    if name_e.get() == "":
        messagebox.showerror("alert","Name field cannot be empty!!!")
    elif contact_e.get() == "":
        messagebox.showerror("alert","Contact field cannot be empty!!!")
    elif email_e.get() == "":
        messagebox.showerror("alert","Email field cannot be empty!!!")
    elif city.get() =="":
        messagebox.showerror("alert","City field cannot be empty!!!")
    elif state.get() =="":
        messagebox.showerror("alert","State field cannot be empty!!!")
    elif Gender.get() =="":
        messagebox.showerror("alert","Gender field cannot be empty!!!")
    else:
        db = pymysql.connect(host = "localhost",user= "root",password="")
        c = db.cursor()
    
        
        query = 'create database IF NOT EXISTS tkinter'
        c.execute(query)
        db.commit()
        print("Database Created Successsfully")
            
        db = pymysql.connect(host = "localhost",user= "root",password="",database="tkinter")
        c = db.cursor()
        
        query1 = 'create table  IF NOT EXISTS registration_form(ID int auto_increment primary key,Name varchar(20), Contact varchar(20), Email varchar(20),Gender varchar(10),City varchar(10), State varchar(10))' 
        c.execute(query1)
        db.commit()
        print("Table Created Successfully")       
            
        c.execute("use tkinter")
        query2 = 'insert into registration_form (Name,  Contact, Email, Gender, City, State) values (%s, %s, %s, %s, %s, %s)'
        # args = (name_e.get(),contact_e.get(),email_e.get(),Gender.get(),city.get(),state.get())
        # c.execute(query2 % args)
        c.execute(query2,(name_e.get(),contact_e.get(),email_e.get(),Gender.get(),city.get(),state.get()))
        db.commit()
        db.close()
        messagebox.showinfo("Success","Data Successfully Written")

# adding all the form data to the database

Name = StringVar()
Contact = StringVar()
Email = StringVar()
Gender = StringVar()
City = StringVar()
State = StringVar()

 

# label for enter details
lbl1 = Label(scr,text="\t\t\tPlease enter details below     \t\t\t",bg="orange",fg="white")
lbl1.place(x=-10,y=2)

# label for name
name = Label(scr,text="Name*",font=("Ariel"))
name.place(x=35,y=55)

name_e = Entry(scr)
name_e.place(x=150,y=59)

# label for contact
contact = Label(scr,text="Contact*",font=("Ariel"))
contact.place(x=35,y=105)

contact_e= Entry(scr)
contact_e.place(x=150,y=108)

# label for email
email = Label(scr,text="Email*",font=("Ariel"))
email.place(x=35,y=155)

email_e = Entry(scr)
email_e.place(x=150,y=158)                                                                                                                              

# radio button
radio_btn = Label(scr,text="Gender*",font=("Ariel"))
radio_btn.place(x=35,y=205)

Gender.set(0)
radio_btn1 = Radiobutton(scr,text="Male",variable = Gender,font="Tahoma",value='Male')
radio_btn1.place(x=140,y=205)

radio_btn2 = Radiobutton(scr,text="Female",variable = Gender,font="Tahoma",value='Female')
radio_btn2.place(x=230,y=205)

# drop down menu

dd_city = Label(scr,text="City*",font="Ariel")
dd_city.place(x=35,y=255)

city = ttk.Combobox(state="readonly",values=["Gandhinagar","Ahmedabad","Rajkot","Surat","Vadodara"])
city.place(x=150,y=257)

dd_state = Label(scr,text="State*",font="Ariel")
dd_state.place(x=35,y=305)

state = ttk.Combobox(state="readonly",values=["Gujarat","Maharashtra","Delhi","Rajasthan","Bangalore"])
state.place(x=150,y=307)

# button display
submit = Button(scr,text="Register",font=("Arial"),fg="black",bg="orange",cursor="hand1",command=sbmt)
submit.place(x=150,y=450)

scr.mainloop()

 
