# product management application

# importing tkinter module
import tkinter
from tkinter import ttk

# create a screen 
scr = tkinter.Tk()

# create a title
scr.title("Registration Form")

# screen size
scr.geometry("400x550")

# label for enter details
lbl1 = tkinter.Label(scr,text="\t\t\tPlease enter details below     \t\t\t",bg="orange",fg="white")
lbl1.place(x=-10,y=2)

# label for name
lbl2 = tkinter.Label(scr,text="Name*",font=("Ariel"))
lbl2.place(x=35,y=55)

e2 = tkinter.Entry(scr)
e2.place(x=150,y=59)

# label for contact
lbl3 = tkinter.Label(scr,text="Contact*",font=("Ariel"))
lbl3.place(x=35,y=105)

e3 = tkinter.Entry(scr)
e3.place(x=150,y=108)

# label for email
lbl4 = tkinter.Label(scr,text="Email*",font=("Ariel"))
lbl4.place(x=35,y=155)

e4 = tkinter.Entry(scr)
e4.place(x=150,y=158)

# radio button

lbl7 = tkinter.Label(scr,text="Gender*",font=("Ariel"),)
lbl7.place(x=35,y=205)

lbl5 = tkinter.Radiobutton(scr,text="Male",font="Ariel",value=1)
lbl5.place(x=140,y=205)

lbl6 = tkinter.Radiobutton(scr,text="Female",font="Ariel",value=2)
lbl6.place(x=230,y=205)

# drop down menu

lbl8 = tkinter.Label(scr,text="City*",font="Ariel")
lbl8.place(x=35,y=255)

lbl9 = ttk.Combobox(state="readonly",values=["Gandhinagar","Ahmedabad","Rajkot","Surat","Vadodara"])
lbl9.place(x=150,y=257)

lbl10 = tkinter.Label(scr,text="State*",font="Ariel")
lbl10.place(x=35,y=305)

lbl11 = ttk.Combobox(state="readonly",values=["Gujarat","Maharashtra","Delhi","Rajasthan","Bangalore"])
lbl11.place(x=150,y=307)

# button display
btn = tkinter.Button(scr,text="Register",font=("Arial"),fg="black",bg="orange")
btn.place(x=150,y=450)


scr.mainloop()



