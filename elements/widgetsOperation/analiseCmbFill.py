from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtWidgets

def analiseCmbData(cmbValue):
    if cmbValue == '' or cmbValue is None:
        return 0
    else:
        symbols = '!@#$%^&*\n|][{}?`~'
        cmbValue = cmbValue.strip()
        for x in symbols:
            cmbValue = cmbValue.replace(x, '')
        cmbValue = cmbValue[0:49]
        return cmbValue


