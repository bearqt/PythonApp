from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont

class MainWindowAdmin(QWidget):
    def __init__(self, login):
        super(MainWindowAdmin, self).__init__()
        self.login = login
        self.setWindowTitle("Admin")
        self.setGeometry(300, 250, 1024, 600)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(350, 50, 400, 100)  # left top width height
        self.label.setText("Пользователи")
        self.label.setFont(QFont("mr_HangingLettersG", 30))

        self.label_user_login = QtWidgets.QLabel(self)
        self.label_user_login.setGeometry(800, 0, 400, 100)
        self.label_user_login.setText("Вы вошли как \nадминистратор " + self.login)
        self.label_user_login.setFont(QFont("Calibri", 10))

        self.table = QTableWidget(self)  # Создаём таблицу
        self.table.setGeometry(10, 150, 400, 400)
        self.table.setColumnCount(4)  # Устанавливаем колонки в таблице
        self.table.setRowCount(self.get_users_length())  # Устанавливаем строки в таблице

        self.table.setHorizontalHeaderLabels(["id", "login", "password", "role"])

        self.editor_label = QtWidgets.QLabel(self)
        self.editor_label.setText("СДЕЛАТЬ РЕДАКТОРОМ")
        self.editor_label.setGeometry(480, 200, 300, 30)
        self.editor_label.setFont(QFont("Typesauce", 12))

        self.editor_input = QtWidgets.QLineEdit(self)
        self.editor_input.setGeometry(QtCore.QRect(500, 250, 250, 30))

        self.editor_button = QtWidgets.QPushButton(self)
        self.editor_button.setGeometry(QtCore.QRect(770, 250, 100, 30))
        self.editor_button.setObjectName("login_button")
        self.editor_button.setText("Добавить")
        self.editor_button.setFont(QFont("Calibri", 10))
        self.editor_button.clicked.connect(self.add_editor)


    def get_users_length(self):
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        users = cursor.execute('''
                                SELECT * FROM users
                                ''').fetchall()
        connection.close()
        return len(users)

    def get_data(self):
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        users = cursor.execute('''
                        SELECT * FROM users
                        ''').fetchall()
        for i in range(len(users)):
            id = str(users[i][0])
            login = users[i][1]
            password = users[i][2]
            role = users[i][3]
            self.table.setItem(i, 0, QTableWidgetItem(id))  # заполняем строки
            self.table.setItem(i, 1, QTableWidgetItem(login))
            self.table.setItem(i, 2, QTableWidgetItem(password))
            self.table.setItem(i, 3, QTableWidgetItem(role))
        self.table.resizeColumnsToContents()  # ресайз колонок по содержимому
        connection.close()

    def add_editor(self):
        id = self.editor_input.text()
        new_role = 'editor'
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        cursor.execute('''
                        UPDATE users SET role = (?) WHERE id = (?)
                                ''', (new_role, id))
        connection.commit()
        connection.close()
        self.get_data()
        self.editor_input.setText("")