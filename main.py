import random
import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import uic

Ui_MainWindown, _ = uic.loadUiType('untitled.ui')


class Ui_MainWindow(Ui_MainWindown,QtWidgets.QMainWindow):
    def init2(self):
        self.paint = None
        self.coords = (None, None)
        self.setMouseTracking(True)
        self.pushButton.clicked.connect(self.func)

    def func(self):
        self.paint = 0
        self.coords = [random.randint(20, self.width()), random.randint(20, self.height())]
        self.repaint()

    def paintEvent(self, event):
        if self.paint is not None:
            qp = QtGui.QPainter()
            qp.begin(self)
            if self.paint == 0:
                self.drawcircle(qp)
            elif self.paint == 1:
                self.drawrect(qp)
            elif self.paint == 2:
                self.drawtrial(qp)
        self.paint = None

    def drawcircle(self, qp):
        if self.coords[0] is not None:
            color = QtGui.QColor(255,255,0)
            qp.setBrush(color)
            x = random.randint(5, 30)
            qp.drawEllipse(self.coords[0] - x, self.coords[1] - x, 2 * x, 2 * x, )

    def drawrect(self, qp):
        if self.coords[0] is not None:
            color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            qp.setBrush(color)
            x = random.randint(5, 30)
            qp.drawRect(self.coords[0] - x, self.coords[1] - x, 2 * x, 2 * x, )

    def drawtrial(self, qp):
        if self.coords[0] is not None:
            color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            qp.setBrush(color)
            x = random.randint(5, 30)
            qp.drawPolygon(QtGui.QPolygon([self.coords[0] - x, self.coords[1] + x, self.coords[0], self.coords[1] - x,
                                           self.coords[0] + x, self.coords[1] + x]), )


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Ui_MainWindow()
    form.setupUi(form)
    form.init2()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
