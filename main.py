from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5 import uic
import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
            qp.setPen(QColor('yellow'))
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
