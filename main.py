import sys

from random import choice
from PyQt5.QtGui import QBrush, QColor, QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("central")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 330, 200, 50))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def btnUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Случайная окружность"))


class Crcl(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Crcl, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.result)
        self.flg = False

    def result(self):
        self.flg = True
        self.update()

    def paintEvent(self, event):
        if self.flg:
            painter = QPainter()
            painter.begin(self)
            self.draw(painter)
            painter.end()

    def draw(self, painter):
        painter.setBrush(QBrush(QColor(choice(range(0, 256)), choice(range(0, 256)), choice(range(0, 256)))))
        painter.setPen(QColor(0, 0, 0))
        x = choice(range(50, 300))
        y = choice(range(50, 300))
        r = choice(range(10, 200))
        painter.drawEllipse(x, y, r, r)
        self.flg = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cnv = Crcl()
    cnv.show()
    sys.exit(app.exec())