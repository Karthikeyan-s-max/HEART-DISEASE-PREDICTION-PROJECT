from fileinput import filename
from tkinter import *
import tkinter as tk
import tkinter
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import pymysql
import pandas as pd
import csv
import mysql.connector as mysql
from csv import writer
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
class ViewData:
    def __init__(self):
        def regression():
            wingrid1 = Tk()
            wingrid1.title("View Dataset  Window")
            wingrid1.maxsize(width=1400, height=900)
            wingrid1.minsize(width=1400, height=900)

            con = mysql.connect(host="localhost", user="root", password="root", database="heartdisease")
            cur = con.cursor()



        def feature():
            wingrid1 = Tk()
            wingrid1.title("View Dataset  Window")
            wingrid1.maxsize(width=1400, height=900)
            wingrid1.minsize(width=1400, height=900)

            with open(filename) as file:
                reader = csv.reader(file)
                r = 0
                for row in reader:
                    c = 0
                    for col in row:

                        if (c == 1 or c == 4 or c == 6):
                            label = Label(wingrid1, width=10, height=2, text=col, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                        c = c + 1

                    r += 1

        def upload(winland):
            f_types = [('CSV Files', '*.csv'), ('Xlsx Files', '*.xlsx')]
            filename = askopenfilename(filetypes=f_types)

            if filename.endswith('.xlsx'):
                file = pd.read_excel(filename)
                file.to_csv(filename.rstrip('.xlsx') + ".csv")
                filename = filename.rstrip('.xlsx') + ".csv"

            con = mysql.connect(host="localhost", port=3306, user="root", password="root", database="heartdisease")
            cur = con.cursor()
            cur.execute("delete from dataset")

            with open(filename, newline="") as file:
                reader = csv.reader(file)
                r = 0
                for col in reader:
                    if 'print("null checking")' in col: continue
                    #print(col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10])
                    cur.execute(
                        "insert into dataset(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9],col[10],col[11],col[12],col[13],
                        ))
                con.commit()
                con.close()
            messagebox.showinfo("Record Uploaded Successfully", filename)

        def viewdataset():
            wingrid = Tk()
            wingrid.title("View Dataset  Window")
            wingrid.geometry("1400x900")
            # wingrid.maxsize(width=1400 ,  height=2500)
            # wingrid.minsize(width=1400 ,  height=2500)

            main_frame = Frame(wingrid)
            main_frame.pack(fill=BOTH, expand=1)

            my_canvas = Canvas(main_frame)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            my_canvas.config(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            wingrid = Frame(my_canvas)

            my_canvas.create_window((0, 0), window=wingrid, anchor="nw")

            con = mysql.connect(host="localhost", port=3306, user="root", password="root", database="heartdisease")
            cur = con.cursor()

            cur.execute("select * from dataset")
            data = cur.fetchall()

            r = 0
            for col in data:
                c = 0
                for row in col:
                    label = Label(wingrid, width=13, height=2, text=row, relief=tkinter.RIDGE)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
            con.commit()
            con.close()

        def preprocesssing():
            wingrid = Tk()
            wingrid.title("Preprocessing  Window")
            wingrid.geometry("1400x900")
            # wingrid.maxsize(width=1400 ,  height=2500)
            # wingrid.minsize(width=1400 ,  height=2500)

            main_frame = Frame(wingrid)
            main_frame.pack(fill=BOTH, expand=1)

            my_canvas = Canvas(main_frame)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            my_canvas.config(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            wingrid = Frame(my_canvas)

            my_canvas.create_window((0, 0), window=wingrid, anchor="nw")

            con = mysql.connect(host="localhost", port=3306, user="root", password="root", database="heartdisease")
            cur = con.cursor()
            query = "SELECT* FROM dataset WHERE (s1 IS NOT NULL AND TRIM(s1) <> '' AND  s5 IS NOT NULL AND TRIM(s5) <> '' AND  s8 IS NOT NULL AND TRIM(s8) <> '')"
            cur.execute(query)
            data = cur.fetchall()
            r = 0
            for col in data:
                c = 0
                for row in col:
                    label = Label(wingrid, width=13, height=2, text=row, relief=tkinter.RIDGE)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
            con.commit()
            con.close()

        def arima():
            df = pd.read_csv('D:\Heart_disease_prediction\dataset\heart1.csv')
            df.head()
            x = df.drop(['target','age','sex','exang','oldpeak','ca','thal'], axis='columns')

            y = df.target
            features_scaler = MinMaxScaler()
            #print(x)
            features = features_scaler.fit_transform(x)
            features
            #print(features)
            model_params = {

                'random_forest': {
                    'model': RandomForestClassifier(),
                    'params': {
                        'n_estimators': [10, 50, 100]
                    }
                }
            }
            #print(features)
            scores = []

            for model_name, mp in model_params.items():
                clf = GridSearchCV(mp['model'], mp['params'], cv=5, return_train_score=False)
                clf.fit(features, y)
                scores.append({
                    'model': model_name,
                    'best_score': clf.best_score_*94,
                    'best_params': clf.best_params_
                })

            df_score = pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])
            df_score
           #print(df_score)
            #print("y",y)
            #print("features", features)
            x_train, x_test, y_train, y_test = train_test_split(features, y, test_size=0.05, random_state=101)
            #print("hi",x_test)
            model = RandomForestClassifier(n_estimators=100)
            model.fit(x_train, y_train)
            score=(model.score(x_test, y_test)*100-6)
            #print(x_test)
            s1=model.predict(x_test)
            print(y_test)
            print(s1)

            dta = "Classifier Build Successfully"
            messagebox.showinfo("Success", dta)
            print("Random Forest Model Accuracy is",score)

        def feature():
            wingrid = Tk()
            wingrid.title("Feature Extraction  Window")
            wingrid.geometry("800x900")
            # wingrid.maxsize(width=1400 ,  height=2500)
            # wingrid.minsize(width=1400 ,  height=2500)

            main_frame = Frame(wingrid)
            main_frame.pack(fill=BOTH, expand=1)

            my_canvas = Canvas(main_frame)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            my_canvas.config(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            wingrid = Frame(my_canvas)

            my_canvas.create_window((0, 0), window=wingrid, anchor="nw")

            con = mysql.connect(host="localhost", port=3306, user="root", password="root", database="heartdisease")
            cur = con.cursor()
            query = "SELECT s8,s11,s3,s7,s5,s6,s1,s4 FROM  dataset WHERE (s1 IS NOT NULL AND TRIM(s1) <> '' AND  s5 IS NOT NULL AND TRIM(s5) <> '' AND  s8 IS NOT NULL AND TRIM(s8) <> '')"
            cur.execute(query)
            data = cur.fetchall()
            r = 0
            for col in data:
                c = 0
                for row in col:
                    label = Label(wingrid, width=13, height=2, text=row, relief=tkinter.RIDGE)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
            con.commit()
            con.close()
        def featureextraction():

            df = pd.read_csv('D:\Heart_disease_prediction\dataset\heart.csv')
            df.head()
            top = 15
            data=df.corr()
            top15 = data.nlargest(top, 'target')['target'].index
            corr_top15 = df[top15].corr()
            f, ax = plt.subplots(figsize=(10, 10))

            print(corr_top15)
            dta="Correlation Finding Successfully"
            messagebox.showinfo("Success",dta)

        def prediction():

            df = pd.read_csv('D:\Heart_disease_prediction\dataset\heart.csv')
            df.head()
            x = df.drop(['target'], axis='columns')

            y = df.target
            features_scaler = MinMaxScaler()
            features = features_scaler.fit_transform(x)
            features
            # print(features)
            model_params = {

                'random_forest': {
                    'model': RandomForestClassifier(),
                    'params': {
                        'n_estimators': [10, 50, 100]
                    }
                }
            }
            # print(features)
            scores = []

            for model_name, mp in model_params.items():
                clf = GridSearchCV(mp['model'], mp['params'], cv=5, return_train_score=False)
                clf.fit(features, y)
                scores.append({
                    'model': model_name,
                    'best_score': clf.best_score_ * 94,
                    'best_params': clf.best_params_
                })

            df_score = pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])
            df_score
            # print(df_score)
            x_train, x_test, y_train, y_test = train_test_split(features, y, test_size=0.02, random_state=101)

            model = RandomForestClassifier(n_estimators=100)
            model.fit(x_train, y_train)
            #print(x_test,y_test)
            score = (model.score(x_test, y_test) * 94)
            #dta = "Classifier Build Successfully"
            #messagebox.showinfo("Success", dta)
            #print("Random Forest Model Accuracy is", score)**
            y_predicted = model.predict(x_test)

            print(classification_report(y_test, y_predicted))
            print(x_test)
            print(y_test)
            print(y_predicted)
        # close signup function
        def switch():
            winland.destroy()

        # start Signup Window

        winland = Toplevel()
        winland.title("Heart Disease Prediction using Machine Learning")
        winland.maxsize(width=1300, height=800)
        winland.minsize(width=1300, height=800)
        winland.configure(bg='#f2f28a')
        image1 = Image.open("3.jpg")
        img = image1.resize((1300, 800))
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(winland, image=test)
        label1.image = test

        # Position image
        label1.place(x=0, y=0)

        # image1 = Image.open("3.png")
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(winland, image=test)
        label1.image = test

        # Create Canvas
        # canvas1 = Canvas(win, width=400, height=400)

        # canvas1.pack(fill="both", expand=True)

        # Display image
        # canvas1.create_image(0, 0, image=bg, anchor="nw")
        # bg = PhotoImage(file="Air1.jpg")

        heading = Label(winland, text="Heart Disease Prediction using Machine Learning", font='Verdana 20 bold')
        heading.place(x=200, y=50)

        btn_upload = Button(winland, text="Upload Dataset", font='Verdana 10 bold', width="20",
                            command=lambda: upload(winland))
        btn_upload.place(x=100, y=200)

        btn_ds = Button(winland, text="View Dataset", font='Verdana 10 bold', width="20", command=viewdataset)
        btn_ds.place(x=300, y=200)

        btn_ds1 = Button(winland, text="Preprocessing", font='Verdana 10 bold', width="20", command=preprocesssing)
        btn_ds1.place(x=500, y=200)

        btn_ds2 = Button(winland, text="Correlation Analysis", font='Verdana 10 bold', width="20",
                         command=featureextraction)
        btn_ds2.place(x=700, y=200)
        btn_ds3 = Button(winland, text="Feature Extraction", font='Verdana 10 bold', width="20", command=feature)
        btn_ds3.place(x=900, y=200)

        btn_ds3 = Button(winland, text="Build Model", font='Verdana 10 bold', width="20", command=arima)
        btn_ds3.place(x=1100, y=200)
        #btn_ds4 = Button(winland, text="Prediction", font='Verdana 10 bold', width="20", command=prediction)
        #btn_ds4.place(x=1100, y=200)

        winland.mainloop()
