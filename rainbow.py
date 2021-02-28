from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5 import uic
import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 530, 91, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Кнопка"))


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.update)
        self.drawing = True
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Желтые круги')
        self.show()

    def paintEvent(self, event):
        if self.drawing:
            qp = QPainter()
            qp.begin(self)
            color_rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setPen(QColor(*color_rgb))
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        s = randint(30, 300)
        f = randint(30, 300)
        qp.drawEllipse(s, s, s + f, s + f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    sys.exit(app.exec_())
