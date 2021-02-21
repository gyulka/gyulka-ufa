import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 388)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 461, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.horizontalSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(100)
        self.horizontalSlider.setPageStep(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.plainTextEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBox_3 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinBox_3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "title"))
        self.label.setText(_translate("Dialog", "stepen"))
        self.label_2.setText(_translate("Dialog", "молотый/зерна"))
        self.plainTextEdit.setPlaceholderText(_translate("Dialog", "description"))
        self.label_3.setText(_translate("Dialog", "price"))
        self.label_4.setText(_translate("Dialog", "objem"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 49, 660, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "добавить"))


class Dialog(Ui_Dialog, QtWidgets.QDialog):
    def init2(self, parent):
        self.par = parent
        self.buttonBox.rejected.connect(self.reject)

    def reject(self):
        super().reject()

    def accept(self):
        self.par.con.execute(
            f'''insert into coffe(title,stepen, zerna, description, price, obj) values("{self.lineEdit.text()}",{self.spinBox.value()},{'true' if self.horizontalSlider.value else 'false'},"{self.plainTextEdit.toPlainText()}",{self.spinBox_2.value()},{self.spinBox_3.value()})''')
        self.par.con.commit()
        super().accept()


class Ui_MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
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
