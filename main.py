import sqlite3
import sys

from PyQt5 import QtWidgets
from PyQt5 import uic

Ui_MainWindown, _ = uic.loadUiType('untitled.ui')
UI_dialog, _ = uic.loadUiType('dialog.ui')


class Dialog(UI_dialog, QtWidgets.QDialog):
    def init2(self, parent):
        self.par = parent
        self.buttonBox.rejected.connect(self.reject)

    def reject(self):
        super().reject()

    def accept(self):
        self.par.con.execute(f'''insert into coffe(title,stepen, zerna, description, price, obj) values("{self.lineEdit.text()}",{self.spinBox.value()},{'true' if self.horizontalSlider.value else 'false'},"{self.plainTextEdit.toPlainText()}",{self.spinBox_2.value()},{self.spinBox_3.value()})''')
        self.par.con.commit()
        super().accept()


class Ui_MainWindow(Ui_MainWindown, QtWidgets.QMainWindow):
    def init2(self):
        self.con = sqlite3.connect('coffe.db')
        self.func()
        self.pushButton.clicked.connect(self.func1)

    def func(self):
        for i in enumerate(self.con.execute(f'''select * from coffe''')):
            self.tableWidget.setRowCount(i[0] + 1)
            self.tableWidget.setColumnCount(len(i[1]))

            for j in enumerate(i[1]):
                self.tableWidget.setItem(i[0], j[0], QtWidgets.QTableWidgetItem(str(j[1])))
        self.tableWidget.setHorizontalHeaderLabels(['id', 'title', 'stepen', 'zerna', 'description', 'price', 'objem'])

    def func1(self):
        self.dialog = Dialog()
        self.dialog.setupUi(self.dialog)
        self.dialog.init2(self)
        self.dialog.exec_()
        self.func()


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
