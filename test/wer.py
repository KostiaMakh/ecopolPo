# Ecopolymer equipment program
import os
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets, QtGui, uic
from elements.sql.connectSql import connectToSql



class WindO(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.connect = connectToSql()
        self.resize(500, 300)


        a = [[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd']]
        vbox = QtWidgets.QFormLayout()

        for i in range(len(a)):
            self.lab = QtWidgets.QLabel(f'Hello {a[i][0]}')
            self.qbt = QtWidgets.QPushButton(f'Her {a[i][1]}')
            vbox.addWidget(self.lab)
            vbox .addWidget(self.qbt)

        self.setLayout(vbox)








if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window =WindO()
    window.show()
    sys.exit(app.exec_())