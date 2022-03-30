# Ecopolymer equipment program
import os
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets, QtGui, uic
from elements.sql.connectSql import connectToSql



class WindO(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.resize(500, 500)

        self.vbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox)

        self.b1 = QtWidgets.QPushButton()
        self.b1.setText('Start')
        self.vbox.addWidget(self.b1)

        self.b1.clicked.connect(self.b1_press)

    def b1_press(self):
        try:
            a = 1/0
            self.cantMake = QtWidgets.QMessageBox()
            self.cantMake.setText(f'a = {a}')
            self.cantMake.setIcon(QtWidgets.QMessageBox.Icon.Information)
            self.cantMake.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.cantMake.show()
        # self.a = QtWidgets.QMessageBox()
        # self.a.setText('Пиздец')
        # self.a.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        # self.a.show()
        except:
            self.cantMake = QtWidgets.QMessageBox()
            self.cantMake.setText('Не удалось выполнить операцию')
            self.cantMake.setIcon(QtWidgets.QMessageBox.Icon.Information)
            self.cantMake.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

            result = self.cantMake.exec_()

            self.cantMake.show()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window =WindO()
    window.show()
    sys.exit(app.exec_())