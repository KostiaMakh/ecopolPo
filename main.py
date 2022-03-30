# Ecopolymer equipment program
import os
import sys
from PyQt5 import QtWidgets
from widgets.objInf_w.objInfoWindow import Window
from elements.mainGlobalObject import mainGlobalObject

from widgets.equipW.equipW import EquipW
# main object contain information about object and equipment

from elements.fileOperation.pushGepParamToCalculation import pushParamsToFile


if __name__ == '__main__':
    # pushParamsToFile('213')
    app = QtWidgets.QApplication(sys.argv)
    qss = 'style/style.css'
    with open(qss, 'r') as cs:
        app.setStyleSheet(cs.read())
    window = Window()
    window.show()
    sys.exit(app.exec_())

