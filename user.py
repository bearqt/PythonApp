from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont

class MainWindowUser(QWidget):
    def __init__(self, login, balance):
        super(MainWindowUser, self).__init__()
        self.login = login
        self.balance = balance
        self.setWindowTitle("User")
        self.setGeometry(300, 250, 1024, 600)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(400, 50, 400, 100)  # left top width height
        self.label.setText("Скачки")
        self.label.setFont(QFont("mr_HangingLettersG", 30))

        self.label_user_login = QtWidgets.QLabel(self)
        self.label_user_login.setGeometry(800, 0, 400, 100)
        self.label_user_login.setText("Вы вошли как " + self.login + "\nВаш баланс: " + str(self.balance))
        self.label_user_login.setFont(QFont("Calibri", 10))

        self.table = QTableWidget(self)  # Создаём таблицу
        self.table.setGeometry(10, 150, 300, 400)
        self.table.setColumnCount(3)  # Устанавливаем колонки в таблице
        self.table.setRowCount(self.races_length())  # Устанавливаем строки в таблице

        self.table.setHorizontalHeaderLabels(["race id", "horse", "ratio"])

        self.label_id = QtWidgets.QLabel(self)
        self.label_id.setGeometry(600, 150, 400, 50)
        self.label_id.setText("ВВЕДИТЕ ID СКАЧКИ")
        self.label_id.setFont(QFont("Typesauce", 12))

        self.id_input = QtWidgets.QLineEdit(self)
        self.id_input.setGeometry(QtCore.QRect(650, 200, 100, 50))

        self.label_money = QtWidgets.QLabel(self)
        self.label_money.setGeometry(610, 250, 400, 50)
        self.label_money.setText("ВВЕДИТЕ СУММУ")
        self.label_money.setFont(QFont("Typesauce", 12))

        self.money_input = QtWidgets.QLineEdit(self)
        self.money_input.setGeometry(QtCore.QRect(630, 300, 150, 50))

        self.button_bet = QtWidgets.QPushButton(self)
        self.button_bet.setGeometry(QtCore.QRect(600, 380, 200, 50))
        self.button_bet.setObjectName("login_button")
        self.button_bet.setText("Сделать ставку")
        self.button_bet.setFont(QFont("Calibri", 10))
        self.button_bet.clicked.connect(self.make_bet)

    def make_bet(self):
        id = self.id_input.text()
        money = self.money_input.text()
        self.balance -= float(money)
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        cursor.execute('''
                    INSERT INTO bets (login, race_id, money) VALUES  (?, ?, ?)
                         ''', (self.login, id, money))
        cursor.execute('''
                            UPDATE users SET balance = (?) WHERE login = (?)
                                ''', (self.balance, self.login))
        connection.commit()
        connection.close()
        self.id_input.setText("")
        self.money_input.setText("")
        self.label_user_login.setText("Вы вошли как " + self.login + "\nВаш баланс: " + str(self.balance))



    def races_length(self):
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        races = cursor.execute('''
                                SELECT race_id FROM races
                                ''').fetchall()
        connection.close()
        return len(races)

    def get_data(self):
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        races = cursor.execute('''
                        SELECT * FROM races
                        ''').fetchall()
        for i in range(len(races)):
            race_id = str(races[i][0])
            horse = races[i][1]
            ratio = str(races[i][2])
            self.table.setItem(i, 0, QTableWidgetItem(race_id))  # заполняем строки
            self.table.setItem(i, 1, QTableWidgetItem(horse))
            self.table.setItem(i, 2, QTableWidgetItem(ratio))
        self.table.resizeColumnsToContents()  # ресайз колонок по содержимому
        connection.close()

