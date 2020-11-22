import sys
import random as rd
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLabel, QLineEdit, \
    QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPolygonF, QPainterPath
from PyQt5.QtCore import QPoint


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 590)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 527, 141, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Paint"))


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.paint)
        self.setWindowTitle('Random circles')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def paint(self):
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)))
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
