from PyQt5 import QtWidgets, QtGui, uic

from widgets.rto_page.rtoWindow import RtoWindow
from widgets.erpe_page.erpeWindow import ErpeWindow
from widgets.rvgo_page.rvgoWindow import RvgoWindow


class EquipW(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.parent = parent
        uic.loadUi("widgets/equipW/equipW.ui", self)

        self.btn_back.clicked.connect(self.back_page)
        self.btn_rto.clicked.connect(self.rto_calc)
        self.btn_erpe.clicked.connect(self.erpe_calc)
        self.btn_rvgo.clicked.connect(self.rvgo_calc)
        # a = QtWidgets.QPushButton('3')
        # a.clicked.connect()

    def back_page(self):
        self.hide()
        self.parent.show()

    def rto_calc(self):
        self.hide()
        rtoPage = RtoWindow(self)
        rtoPage.show()

    def erpe_calc(self):
        self.hide()
        erpePage = ErpeWindow(self)
        erpePage.show()

    def rvgo_calc(self):
        self.hide()
        rvgoPage = RvgoWindow(self)
        rvgoPage.show()
