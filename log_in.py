from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont

from sign_up import SignUpWindow
from admin import MainWindowAdmin
from editor import MainWindowEditor
from user import MainWindowUser

class LogInWindow(QWidget):
    def __init__(self):
        super(LogInWindow, self).__init__()
        self.setWindowTitle("Log in")
        self.setGeometry(300, 250, 1024, 600)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(360, 50, 400, 100)  # left top width height
        self.label.setText("Авторизация")
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

        self.login_button = QtWidgets.QPushButton(self)
        self.login_button.setGeometry(QtCore.QRect(430, 300, 191, 41))
        self.login_button.setObjectName("login_button")
        self.login_button.setText("Войти")
        self.login_button.setFont(QFont("Calibri", 10))
        self.login_button.clicked.connect(self.log_in)

        self.signup_button = QtWidgets.QPushButton(self)
        self.signup_button.setGeometry(QtCore.QRect(400, 350, 251, 41))
        self.signup_button.setObjectName("signup_button")
        self.signup_button.setText("Зарегистрироваться")
        self.signup_button.setFont(QFont("Calibri", 10))
        self.signup_button.clicked.connect(self.sign_up)

    def sign_up(self):
        self.sign_up_window = SignUpWindow()
        self.sign_up_window.show()

    def log_in(self):
        login = self.login_input.text()
        password = self.password_input.text()
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        array = cursor.execute('''
                        SELECT role, balance FROM users WHERE login = (?) AND password = (?)
                        ''', (login, password)).fetchall()
        if array != []:
            if array[0][0] == 'admin':
                self.login_input.setText("")
                self.password_input.setText("")
                self.admin_window = MainWindowAdmin(login)
                self.admin_window.get_data()
                self.admin_window.show()
            elif array[0][0] == 'editor':
                self.login_input.setText("")
                self.password_input.setText("")
                self.editor_window = MainWindowEditor(login)
                self.editor_window.get_races_data()
                self.editor_window.get_bets_data()
                self.editor_window.show()
            elif array[0][0] == 'user':
                self.login_input.setText("")
                self.password_input.setText("")
                self.user_window = MainWindowUser(login, array[0][1])
                self.user_window.get_data()
                self.user_window.show()
        else:
            self.login_input.setText("Неверный логин")
            self.password_input.setText("Неверный пароль")

        connection.commit()
        connection.close()