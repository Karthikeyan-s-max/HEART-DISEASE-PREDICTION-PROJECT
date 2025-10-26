from tkinter import *
import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd
import csv
from csv import writer
from tkinter import simpledialog
import numpy as np
import pandas as pd
import statsmodels.api as sm
import warnings

warnings.filterwarnings("ignore")
# Data Visualisation
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.model_selection import train_test_split


# ------------------------------------------------------------ Main Window -----------------------------------------
class ViewLand:
    def __init__(self):
        # area, sub area - fore cast btn 2020-2030 (mean and area ) , variance , real estate fore cast analysis

        def viewdataset():
            wingrid = Tk()
            wingrid.title("View Dataset  Window")
            wingrid.maxsize(width=1400, height=900)
            wingrid.minsize(width=1400, height=900)
            userinput = simpledialog.askstring(title="Regression Values", prompt="Enter Area Name :")



        win = Toplevel()
        win.title("Heart Disease Prediction using Machine Learning")
        win.maxsize(width=1100, height=1000)
        win.minsize(width=1100, height=1000)
        bg = PhotoImage(file="Apps5.png")


        # Create Canvas
        canvas1 = Canvas(win, width=400, height=400)

        canvas1.pack(fill="both", expand=True)

        # Display image
        canvas1.create_image(0, 0, image=bg, anchor="nw")

        # heading label
        heading = Label(win, text="Heart Disease Prediction using Machine Learning", font='Verdana 20 bold')
        heading.place(x=350, y=50)

        btn_ds = Button(win, text="Test Dataset", font='Verdana 10 bold', width="20", command=viewdataset)
        btn_ds.place(x=600, y=200)

        btn_exit = Button(win, text="Exit", font='Verdana 10 bold', width="20", command=quit)
        btn_exit.place(x=600, y=300)

        win.mainloop()
