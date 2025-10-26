from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
import random
import pymysql
import numpy as np
import pandas as pd
import statsmodels.api as sm
import warnings

from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")
# Data Visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# from  Landdetails import LandDet
# from viewdetails import ViewLand
from dataview import ViewData


class Login:
    def __init__(self):

        def checklogin():
            if useridentry.get() == "" and passwordentry.get() == "":
                messagebox.showerror("Error", "Enter User id", parent=winlogin)
            elif useridentry.get() == "karthi" and passwordentry.get() == "karthi":
                land = ViewData()
            else:
                try:
                    con = pymysql.connect(host="localhost", port=3306, user="root", password="root",
                                          database="heartdisease")
                    cur = con.cursor()

                    cur.execute("select username,password from user_information where username=%s and password=%s ",
                                (useridentry.get(), passwordentry.get()))
                    row = cur.fetchone()

                    if row == None:
                        messagebox.showerror("Error", "Invalid User id", parent=winlogin)

                    else:
                        messagebox.showinfo("Success", "Successfully Login", parent=winlogin)
                        con.close()
                        # exec(open("Test1.py").read())


                except Exception as es:
                    messagebox.showerror("Error", f"Error Duo toooo : {str(es)}", parent=winlogin)

        winlogin = Toplevel()
        winlogin.title("Login Window")
        winlogin.maxsize(width=900, height=900)
        winlogin.minsize(width=900, height=900)
        winlogin.configure(bg='#f2f28a')

        image1 = Image.open("4.jpg")
        img = image1.resize((900, 900))
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(winlogin, image=test)
        label1.image = test


        label1.place(x=0, y=0)


        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(winlogin, image=test)
        label1.image = test


        heading = Label(winlogin, text="Heart Disease Prediction ", font='Verdana 20 bold')
        heading.place(x=200, y=50)

        # heading label
        heading = Label(winlogin, text="Login", font='Verdana 15 bold')
        heading.place(x=80, y=60)

        # form data label
        userid = Label(winlogin, text="User Name :", font='Verdana 10 bold')
        userid.place(x=80, y=130)

        # form data label
        password = Label(winlogin, text="Password :", font='Verdana 10 bold')
        password.place(x=80, y=180)

        # Entry Box
        userid = StringVar()
        password = StringVar()
        useridentry = Entry(winlogin, width=40, textvariable=userid)
        useridentry.focus()
        useridentry.place(x=200, y=130)

        passwordentry = Entry(winlogin, width=40, show='*', textvariable=password)
        passwordentry.focus()
        passwordentry.place(x=200, y=180)

        # button login and clear

        btn_login = Button(winlogin, text="Login", font='Verdana 10 bold', command=checklogin)
        btn_login.place(x=200, y=240)

        btn_exit = Button(winlogin, text="Exit", font='Verdana 10 bold', command=quit)
        btn_exit.place(x=300, y=240)

        winlogin.mainloop()
