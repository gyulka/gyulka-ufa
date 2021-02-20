import sqlite3
import sys

from PyQt5 import QtWidgets
from PyQt5 import uic

Ui_MainWindown, _ = uic.loadUiType('untitled.ui')


class Ui_MainWindow(Ui_MainWindown, QtWidgets.QMainWindow):
    def init2(self):
        self.con = sqlite3.connect('coffe.db')
        self.func()

    def func(self):
        for i in enumerate(self.con.execute(f'''select * from coffe''')):
            self.tableWidget.setRowCount(i[0] + 1)
            self.tableWidget.setColumnCount(len(i[1]))

            for j in enumerate(i[1]):
                self.tableWidget.setItem(i[0], j[0], QtWidgets.QTableWidgetItem(str(j[1])))
        self.tableWidget.setHorizontalHeaderLabels(['id', 'title', 'stepen', 'zerna', 'description', 'price', 'objem'])


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
