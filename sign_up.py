from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont

class SignUpWindow(QWidget):
    def __init__(self):
        super(SignUpWindow, self).__init__()
        self.setWindowTitle("Sign Up")
        self.setGeometry(300, 250, 1024, 600)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(360, 50, 400, 100)  # left top width height
        self.label.setText("Регистрация")
        self.label.setFont(QFont("mr_HangingLettersG", 30))

        self.login_input = QtWidgets.QLineEdit(self)
        self.login_input.setGeometry(QtCore.QRect(350, 200, 311, 20))
        self.login_input.setObjectName("login_input")

        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setGeometry(QtCore.QRect(350, 250, 311, 20))
        self.password_input.setObjectName("password_input")

        self.login_label = QtWidgets.QLabel(self)
        self.login_label.setText("ЛОГИН")
        self.login_label.setGeometry(250, 185, 80, 50)
        self.login_label.setFont(QFont("Typesauce", 10))

        self.password_label = QtWidgets.QLabel(self)
        self.password_label.setText("ПАРОЛЬ")
        self.password_label.setGeometry(250, 235, 80, 50)
        self.password_label.setFont(QFont("Typesauce", 10))

        self.signup_button = QtWidgets.QPushButton(self)
        self.signup_button.setGeometry(QtCore.QRect(400, 350, 251, 41))
        self.signup_button.setObjectName("signup_button")
        self.signup_button.setText("Зарегистрироваться")
        self.signup_button.setFont(QFont("Calibri", 10))
        self.signup_button.clicked.connect(self.sign_up)

    def sign_up(self):
        login = self.login_input.text()
        password = self.password_input.text()
        role = 'user'
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        cursor.execute('''
                        INSERT INTO users (login, password, role, balance) VALUES (?, ?, ?, ?)
                        ''', (login, password, role, "1000"))
        connection.commit()
        connection.close()
        self.login_input.setText("")
        self.password_input.setText("")