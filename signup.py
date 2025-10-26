from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

import pandas as pd
from PIL import Image, ImageTk
import random
import pymysql
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor

from login import Login


class Signup:
    def __init__(self):

        # signup database connect
        def action():
            s1 = userid.get()
            s2 = username.get()
            s3 = password.get()
            s4 = address.get()
            s5 = emailid.get()
            s6 = mobile.get()



            df = pd.read_csv('D:\Heart_disease_prediction\dataset\heart.csv')
            df.head()
            m1 = RandomForestRegressor()

            result1 = ([[userid.get(), username.get(), password.get(), address.get(), emailid.get(),
                         mobile.get()]])
            cp = int(userid.get())
            trestbs = int(username.get())
            chol = int(password.get())
            fbs = int(address.get())
            restecg = int(emailid.get())
            thalach = int(mobile.get())


            if cp>=1 and trestbs >=130 and chol>=230 and fbs>=1 and thalach>=110:
                print("Heart disease")
                result="Person seems to Heart Disease"
                messagebox.showinfo("Result",result)

            else  :
                print("Bad")
                result = "Person Seems to Normal"
                messagebox.showinfo("Result",result)

        # close signup function
        def switch():
            exec(open("Test2.py").read())

        # clear data function
        def clear():
            userid.delete(0, END)
            username.delete(0, END)
            address.delete(0, END)
            emailid.delete(0, END)
            mobile.delete(0, END)
            password.delete(0, END)



            # start Signup Window

        winsignup = Toplevel()
        winsignup.title("login Window")
        winsignup.maxsize(width=900, height=900)
        winsignup.minsize(width=900, height=900)
        winsignup.configure(bg='#f2f28a')
        image1 = Image.open("2.jpg")
        img = image1.resize((1100, 900))
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(winsignup, image=test)
        label1.image = test

        # Position image
        label1.place(x=0, y=0)

        # image1 = Image.open("3.png")
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(winsignup, image=test)
        label1.image = test

        heading = Label(winsignup, text="Heart Disease Prediction using Machine Learning", font='Verdana 20 bold')
        heading.place(x=80, y=50)

        # heading label

        # form data label
        userid = Label(winsignup, text="CP:", font='Verdana 10 bold')
        userid.place(x=80, y=130)

        username = Label(winsignup, text="Trestbps :", font='Verdana 10 bold')
        username.place(x=80, y=160)

        password = Label(winsignup, text="Cholestrol:", font='Verdana 10 bold')
        password.place(x=80, y=190)

        address = Label(winsignup, text="FBS :", font='Verdana 10 bold')
        address.place(x=80, y=240)

        emailid = Label(winsignup, text="Restecg :", font='Verdana 10 bold')
        emailid.place(x=80, y=290)

        mobile = Label(winsignup, text="Thalach :", font='Verdana 10 bold')
        mobile.place(x=80, y=320)

        # Entry Box ------------------------------------------------------------------

        userid = StringVar()
        username = StringVar()
        password = StringVar()
        address = StringVar()
        emailid = StringVar()
        mobile = StringVar()



        userid = Entry(winsignup, width=40, textvariable=userid)
        userid.focus()
        userid.place(x=230, y=130)

        username = Entry(winsignup, width=40, textvariable=username)
        username.focus()
        username.place(x=230, y=160)

        password = Entry(winsignup, width=40, textvariable=password)
        password.place(x=230, y=190)

        address = Entry(winsignup, width=40, textvariable=address)
        address.place(x=230, y=240)

        emailid = Entry(winsignup, width=40, textvariable=emailid)
        emailid.place(x=230, y=290)

        mobile = Entry(winsignup, width=40, textvariable=mobile)
        mobile.place(x=230, y=320)


        # button login and clear

        btn_signup = Button(winsignup, text="Prediction", font='Verdana 10 bold', command=action)
        btn_signup.place(x=200, y=440)

        btn_login = Button(winsignup, text="Clear", font='Verdana 10 bold', command=clear)
        btn_login.place(x=320, y=440)

        #sign_up_btn = Button(winsignup, text="Forecasting", font='Verdana 10 bold', command=switch)
        #sign_up_btn.place(x=390, y=420)

        winsignup.mainloop()
