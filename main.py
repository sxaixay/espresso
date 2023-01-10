import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.coffee_table = None
        uic.loadUi('main.ui', self)
        self.coffee_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table()

    def load_table(self):
        self.coffee_table.setRowCount(0)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM coffee').fetchall()
        self.coffee_table.setRowCount(len(data))
        for rows, row in enumerate(data):
            for stri in range(len(row)):
                mean = str(row[stri])
                subj = QTableWidgetItem(mean)
                subj.setFlags(Qt.ItemIsEnabled)
                self.coffee_table.setItem(rows, stri, subj)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    sys.exit(app.exec())