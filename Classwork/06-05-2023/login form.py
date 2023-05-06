# importing the module
import tkinter

# making a screen
screen = tkinter.Tk()

# geometry of the form screen
screen.geometry("500x500")

# giving a title
screen.title("Form")

# tkinter variable
email_var = tkinter.StringVar()
password_var = tkinter.StringVar()
msg_var = tkinter.StringVar()

# python function
def myfunc():
    msg_var.set(email_var.get())
    # msg_var.set(password_var.get())

# label display
lbl = tkinter.Label(screen,text="Login Form",font=("Arial",26,"bold"))
lbl.pack()

# email display
e1_lbl=tkinter.Label(screen,text="Enter Email",font=("Arial",16,"bold"))
e1_lbl.place(x=50,y=75)

e1 = tkinter.Entry(screen,textvariable=email_var)
e1.place(x=280,y=75)


# password display
e2_lbl = tkinter.Label(screen,text="Enter Password",font=("Arial",16,"bold"))
e2_lbl.place(x=50,y=115)

e2 = tkinter.Entry(screen,textvariable=password_var)
e2.place(x=280,y=115)


# button display
btn = tkinter.Button(screen,text="SIGN IN",font=("Arial",16,"bold"),fg="black",bg="white",command=myfunc)
btn.place(x=180,y=150)

# message display
msg_lbl = tkinter.Label(screen,text="MESSAGE",textvariable=msg_var)
msg_lbl.place(x=180,y=200)

screen.mainloop()