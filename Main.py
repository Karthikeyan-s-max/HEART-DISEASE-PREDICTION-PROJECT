from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random

from signup import Signup
from login import Login


# ------------------------------------------------------------ Main Window -----------------------------------------
def Signupmeth():
    sign = Signup()


def Loginmeth():
    log = Login()


win = Tk()

# app title
win.title("Heart Disease Prediction using Machine Learning")
win.maxsize(width=1100, height=900)
win.minsize(width=1100, height=900)
win.configure(bg='#f2f28a')
image1 = Image.open("heart.jpg")
img = image1.resize((1100, 900))
test = ImageTk.PhotoImage(img)

label1 = tk.Label(win, image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)

# image1 = Image.open("3.png")
test = ImageTk.PhotoImage(img)

label1 = tk.Label(win, image=test)
label1.image = test





# heading label
heading = Label(win, text="Heart Disease Prediction using Machine Learning", font='Verdana 20 bold')
heading.place(x=150, y=50)

btn_signup = Button(win, text="Admin", font='Verdana 10 bold', width="20", command=Loginmeth)
btn_signup.place(x=400, y=200)
btn_signup = Button(win, text="Prediction", font='Verdana 10 bold', width="20", command=Signupmeth)
btn_signup.place(x=400, y=250)

btn_exit = Button(win, text="Exit", font='Verdana 10 bold', width="20", command=quit)
btn_exit.place(x=400, y=300)

win.mainloop()
