import sys
import random as rd
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit, QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPolygonF, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QPoint


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("UI.ui", self)

        self.pushButton.clicked.connect(self.paint)
        self.setWindowTitle('Yellow circles')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def paint(self):
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor(255, 179, 0))
        size = rd.randint(10, 100)
        x = rd.randint(10, 530)
        y = rd.randint(10, 570)

        qp.drawEllipse(x, y, size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
