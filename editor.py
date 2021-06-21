from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont

class MainWindowEditor(QWidget):
    def __init__(self, login):
        super(MainWindowEditor, self).__init__()
        self.login = login
        self.setWindowTitle("Editor")
        self.setGeometry(300, 250, 1024, 600)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(300, 50, 500, 100)  # left top width height
        self.label.setText("Результаты скачек")
        self.label.setFont(QFont("mr_HangingLettersG", 30))

        self.label_editor_login = QtWidgets.QLabel(self)
        self.label_editor_login.setGeometry(800, 0, 400, 100)
        self.label_editor_login.setText("Вы вошли как \nредактор " + self.login)
        self.label_editor_login.setFont(QFont("Calibri", 10))

        self.label_editor_id = QtWidgets.QLabel(self)
        self.label_editor_id.setGeometry(440, 150, 230, 50)
        self.label_editor_id.setText("ВВЕДИТЕ ID СТАВКИ")
        self.label_editor_id.setFont(QFont("Typesauce", 10))

        self.id_bet_input = QtWidgets.QLineEdit(self)
        self.id_bet_input.setGeometry(QtCore.QRect(490, 200, 100, 30))

        self.win_button = QtWidgets.QPushButton(self)
        self.win_button.setGeometry(QtCore.QRect(440, 250, 100, 30))
        self.win_button.setObjectName("win_button")
        self.win_button.setText("Выигрыш")
        self.win_button.setFont(QFont("Calibri", 10))
        self.win_button.clicked.connect(self.win)

        self.lose_button = QtWidgets.QPushButton(self)
        self.lose_button.setGeometry(QtCore.QRect(560, 250, 100, 30))
        self.lose_button.setObjectName("lose_button")
        self.lose_button.setText("Проигрыш")
        self.lose_button.setFont(QFont("Calibri", 10))
        self.lose_button.clicked.connect(self.lose)

        self.label_editor_races = QtWidgets.QLabel(self)
        self.label_editor_races.setGeometry(440, 350, 250, 50)
        self.label_editor_races.setText("ДОБАВИТЬ ЛОШАДЬ")
        self.label_editor_races.setFont(QFont("Typesauce", 10))

        self.label_name_horse = QtWidgets.QLabel(self)
        self.label_name_horse.setGeometry(420, 380, 200, 50)
        self.label_name_horse.setText("имя лошади")
        self.label_name_horse.setFont(QFont("Typesauce", 7))

        self.horse_input = QtWidgets.QLineEdit(self)
        self.horse_input.setGeometry(QtCore.QRect(420, 420, 100, 30))

        self.label_ratio = QtWidgets.QLabel(self)
        self.label_ratio.setGeometry(570, 380, 200, 50)
        self.label_ratio.setText("коэффициент")
        self.label_ratio.setFont(QFont("Typesauce", 7))

        self.ratio_input = QtWidgets.QLineEdit(self)
        self.ratio_input.setGeometry(QtCore.QRect(570, 420, 100, 30))

        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setGeometry(QtCore.QRect(490, 460, 100, 30))
        self.add_button.setText("Добавить")
        self.add_button.setFont(QFont("Calibri", 10))
        self.add_button.clicked.connect(self.add_race)

        self.table_races = QTableWidget(self)  # Создаём таблицу
        self.table_races.setGeometry(700, 150, 300, 400)
        self.table_races.setColumnCount(3)  # Устанавливаем колонки в таблице
        self.table_races.setRowCount(self.get_races_length())  # Устанавливаем строки в таблице

        self.table_races.setHorizontalHeaderLabels(["race id", "horse", "ratio"])

        self.table_bets = QTableWidget(self)  # Создаём таблицу
        self.table_bets.setGeometry(10, 150, 400, 400)
        self.table_bets.setColumnCount(5)  # Устанавливаем колонки в таблице
        self.table_bets.setRowCount(self.get_bets_length())  # Устанавливаем строки в таблице

        self.table_bets.setHorizontalHeaderLabels(["bet id", "login", "race id", "money", "win"])

    def get_races_length(self):
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        races = cursor.execute('''
                                SELECT * FROM races
                                ''').fetchall()
        connection.close()
        return len(races)

    def get_races_data(self):
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
            self.table_races.setItem(i, 0, QTableWidgetItem(race_id))  # заполняем строки
            self.table_races.setItem(i, 1, QTableWidgetItem(horse))
            self.table_races.setItem(i, 2, QTableWidgetItem(ratio))

        self.table_races.resizeColumnsToContents()  # ресайз колонок по содержимому
        connection.close()

    def get_bets_length(self):
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        bets = cursor.execute('''
                                   SELECT * FROM bets
                                   ''').fetchall()
        connection.close()
        return len(bets)

    def get_bets_data(self):
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        bets = cursor.execute('''
                            SELECT * FROM bets
                            ''').fetchall()
        for i in range(len(bets)):
            bet_id = str(bets[i][0])
            login = bets[i][1]
            race_id = str(bets[i][2])
            money = str(bets[i][3])
            win = str(bets[i][4])
            self.table_bets.setItem(i, 0, QTableWidgetItem(bet_id))  # заполняем строки
            self.table_bets.setItem(i, 1, QTableWidgetItem(login))
            self.table_bets.setItem(i, 2, QTableWidgetItem(race_id))
            self.table_bets.setItem(i, 3, QTableWidgetItem(money))
            if win == "None":
                self.table_bets.setItem(i, 4, QTableWidgetItem("---"))
            else:
                self.table_bets.setItem(i, 4, QTableWidgetItem(win))

        self.table_bets.resizeColumnsToContents()  # ресайз колонок по содержимому
        connection.close()

    def add_race(self):
        horse_name = self.horse_input.text()
        ratio = self.ratio_input.text()
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        cursor.execute('''
                       INSERT INTO races (horse, ratio) VALUES (?, ?)
                     ''', (horse_name, ratio))
        connection.commit()
        connection.close()
        self.table_races.setRowCount(self.get_races_length())
        self.get_races_data()
        self.horse_input.setText("")
        self.ratio_input.setText("")

    def win(self):
        bet_id = str(self.id_bet_input.text())
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        bet = cursor.execute('''
                        SELECT race_id, money, login FROM bets WHERE bet_id = (?)
                        ''', (bet_id,)).fetchall()[0]
        race_id = bet[0]
        money = bet[1]
        login = bet[2]
        ratio = cursor.execute('''
                                SELECT ratio FROM races WHERE race_id = (?)
                                ''', (race_id,)).fetchall()[0][0]
        win = money + money * ratio
        cursor.execute('''
                        UPDATE bets SET win = (?)  WHERE bet_id = (?)
                        ''', (win, bet_id))
        cursor.execute('''
                        UPDATE users SET balance = balance + (?) WHERE login = (?)
                        ''', (win, login))
        connection.commit()
        connection.close()
        self.get_bets_data()
        self.id_bet_input.setText("")

    def lose(self):
        bet_id = str(self.id_bet_input.text())
        import sqlite3
        connection = sqlite3.connect("database.sqlite")
        cursor = connection.cursor()
        win = "0"
        cursor.execute('''
                         UPDATE bets SET win = (?)  WHERE bet_id = (?)
                        ''', (win, bet_id))
        connection.commit()
        connection.close()
        self.get_bets_data()
        self.id_bet_input.setText("")
