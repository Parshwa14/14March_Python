# importing the module
import tkinter

# making a screen 
screen = tkinter.Tk()

# geometry of the screen
screen.geometry("750x750")

# title 
screen.title("Form")

# tkinter variable
email_var = tkinter.StringVar()
pass_var = tkinter.StringVar()
id_var = tkinter.StringVar()
msg_var1 = tkinter.StringVar()

def func():
    msg_var1.set(id_var.get())
    msg_var2 = "Student ID : "
lbl = tkinter.Label(screen,text="Student Registration Form",font=("Arial",25,"bold"))
lbl.pack()

# for student id  

lbl_id = tkinter.Label(screen,text="Student Id",font=("Arial",16,"bold"))
lbl_id.place(x=100,y=100)

e1 = tkinter.Entry(screen,textvariable=id_var)
e1.place(x=280,y=105)

# for student email id
lbl_email = tkinter.Label(screen,text="Student Email",font=("Arial",16,"bold"))
lbl_email.place(x=100,y=150)

e2 = tkinter.Entry(screen,textvariable=email_var)
e2.place(x=280,y=155)

# for student password
lbl_password = tkinter.Label(screen,text="Password",font=("Arial",16,"bold"))
lbl_password.place(x=100,y=200)

e3 = tkinter.Entry(screen,textvariable=pass_var)
e3.place(x=280,y=205)


# button
btn = tkinter.Button(screen,text="Sign In",font=("Arial",16,"bold"),fg="black",bg="orange",command=func)
btn.place(x=250,y=300)

# for message

msg_lbl = tkinter.Label(screen,text="MESSAGE",textvariable=msg_var1)
msg_lbl.place(x=300,y=450)

# display the screen 
screen.mainloop()