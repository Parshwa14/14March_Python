# importing tkinter module
import tkinter

# creating screen
screen = tkinter.Tk()

screen.title("My Application")

screen.geometry("800x800")

def func1():
    print("Calling...")


def func3():
    print("Texting...")


lbl = tkinter.Label(screen,text = "Hello, Welcome to my application",font=("Arial",15,"bold"))
lbl.place(x=50,y=70)

btn1 = tkinter.Button(screen,text="Call ",font=("Arial",20,"bold"),bg="blue",fg="white",command=func1)
btn1.grid(row=0,column=0)


btn3 = tkinter.Button(screen,text="text",font=("Arial",20,"bold"),bg="blue",fg="white",command=func3)
btn3.place(x=100,y=0)
screen.mainloop()