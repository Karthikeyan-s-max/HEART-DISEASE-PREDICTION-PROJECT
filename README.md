# ❤️ Heart Disease Prediction using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg)](https://scikit-learn.org/)
[![MySQL](https://img.shields.io/badge/MySQL-005C84?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey.svg)](https://docs.python.org/3/library/tkinter.html)

A desktop application built with Python and Tkinter that leverages Machine Learning (Random Forest Classifier) to predict the likelihood of heart disease based on patient medical data.

---

## 📌 Project Overview
Cardiovascular diseases are the leading cause of death globally. Early detection is crucial for prevention and treatment. This project provides an intuitive Graphical User Interface (GUI) where administrators can upload medical datasets, preprocess the data, extract important features, perform correlation analysis, and train a Machine Learning model to predict heart disease risk.

## ✨ Key Features
- **User Authentication:** Admin login and signup functionality securely backed by a MySQL database.
- **Dataset Management:** Upload `.csv` or `.xlsx` datasets directly through the GUI and view them in real-time.
- **Data Preprocessing:** Automatically clean data, handle missing values, and scale features using `MinMaxScaler`.
- **Feature Extraction & Analysis:** Discover top correlated features using Pandas and visualize them using Matplotlib.
- **Model Building:** Utilizes **Random Forest Classifier** with `GridSearchCV` for hyperparameter tuning to ensure high accuracy.
- **Interactive GUI:** Easy-to-use desktop interface built with `Tkinter`, making ML accessible to non-technical users.

## 🛠️ Technology Stack
- **Programming Language:** Python
- **GUI Framework:** Tkinter
- **Machine Learning:** Scikit-Learn (Random Forest, Data Preprocessing, Model Evaluation)
- **Data Manipulation & Visualization:** Pandas, NumPy, Matplotlib
- **Database:** MySQL (using `mysql-connector-python` & `pymysql`)

## 🏗️ System Architecture & Workflow
1. **Login/Signup:** Secure admin access.
2. **Data Ingestion:** Upload raw medical dataset (`heart.csv`).
3. **Preprocessing:** Clean dataset and scale numerical features.
4. **Correlation Analysis:** Find the top 15 features most strongly correlated with the target variable.
5. **Model Training:** The system splits the data and trains a optimized Random Forest Classifier.
6. **Prediction:** Evaluate test data and display prediction accuracy.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- MySQL Server (e.g., XAMPP, WAMP, or standalone MySQL)

### 1. Database Setup
1. Open your MySQL client (e.g., phpMyAdmin, MySQL Workbench).
2. Create a new database named `heartdisease`.
3. Import the provided `heartdisease.sql` file to set up the required tables (`dataset` and `user_information`).

### 2. Installation
1. Clone this repository or extract the project folder.
2. Open a terminal/command prompt in the project directory.
3. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install the required Python packages:
   ```bash
   pip install pandas numpy scikit-learn matplotlib pymysql mysql-connector-python Pillow openpyxl
   ```

### 3. Running the Application
Ensure your MySQL server is running, then execute the main Python file:
```bash
python Main.py
```
The desktop GUI will launch, allowing you to log in or register.

---

## 📸 Screenshots
*(You can add screenshots of your GUI here to make your portfolio stand out!)*
- `Login Screen`
- `Dataset View`
- `Model Building & Accuracy`

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## 📜 License
This project is for educational and portfolio purposes.
