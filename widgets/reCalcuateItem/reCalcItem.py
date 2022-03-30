import qtawesome
from PyQt5 import QtWidgets, QtGui, uic, QtCore
from elements.sql.pushToCmbFromSql import getUniqFromColumn
from elements.sql.connectSql import connectToSql
from elements.sql.updateParamInSql import updateParamsInSQL
from elements.widgetsOperation.addPositionToCmb import addPositionToCMB
from elements.sql.renewProposal import get_arh_proposal, get_eqiup_params
from elements.sql.getsQuery import get_all_params_rto

class RecalculationItem(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.resize(1200, 800)
        self.setWindowTitle('Обновить предложения')

        self.tab_widget = QtWidgets.QWidget()
        self.tab_layout = QtWidgets.QVBoxLayout()
        self.table = QtWidgets.QTableWidget()

        self.tab_layout.addWidget(self.table)
        self.tab_widget.setLayout(self.tab_layout)
        self.setCentralWidget(self.tab_widget)

        self.but_widget = QtWidgets.QWidget()
        self.but_layout = QtWidgets.QHBoxLayout()
        self.but_cancel = QtWidgets.QPushButton('Отменить')
        self.but_calc = QtWidgets.QPushButton('Рассчитать')
        self.but_layout.addWidget(self.but_calc)
        self.but_calc.clicked.connect(self.collect_data_from_table)
        self.but_layout.addWidget(self.but_cancel)
        self.but_widget.setLayout(self.but_layout)

        self.tab_layout.addWidget(self.but_widget)

        self.arhive = get_arh_proposal()

        self.table.setRowCount(self.arhive.__len__())
        self.table.setColumnCount(self.arhive[0].__len__())
        headers = ['id', 'Город', 'Объект', 'Локация', 'Позиция по проекту', 'Маркировка', 'Дата', 'Код оборудования', 'Статус']
        self.table.setHorizontalHeaderLabels(headers)
        self.table.hideColumn(7)
        self.table.hideColumn(8)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnWidth(3, 200)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 170)
        self.table.setColumnWidth(6, 140)

        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setWordWrap(True)

        self.add_items_into_table(self.arhive)

    def add_items_into_table(self, arr):
        arr = tuple(reversed(arr))
        for x in range(arr.__len__()):
            for y in range(arr[x].__len__()):
                if y == 0:
                    self.cb = QtWidgets.QCheckBox(str(arr[x][y]))
                    self.table.setCellWidget(x, y, self.cb)
                    self.cb.setObjectName(str(arr[x][y]))
                    self.cb.stateChanged.connect(self.change_row_background_color)
                elif y == 8:
                    self.table.setItem(x, y, QtWidgets.QTableWidgetItem(str(arr[x][y])))
                    if int(arr[x][y]) == 1:
                        for n in range(1, self.table.columnCount()):
                            self.table.cellWidget(x, 0).setStyleSheet("background-color: rgb(224, 224, 224); color: rgb(204, 0, 0); font-style:italic")
                            self.table.item(x, n).setBackground(QtGui.QColor(224, 224, 224))
                            self.table.item(x, n).setForeground(QtGui.QColor(204, 0, 0))
                            self.table.item(x, n).setFont(QtGui.QFont(QtWidgets.QApplication.font().family(), italic=True))
                else:
                    self.table.setItem(x, y, QtWidgets.QTableWidgetItem(str(arr[x][y])))
        self.table.resizeRowsToContents()

    def change_row_background_color(self):
        elem = self.table.cellWidget(self.table.currentRow(), 0)
        for n in range(1, self.table.columnCount()):
            if elem.isChecked() == True:
                self.table.cellWidget(self.table.currentRow(), 0).setStyleSheet("""background-color: rgb(100, 149, 237);""")
                self.table.item(self.table.currentRow(), n).setBackground(QtGui.QColor(100, 149, 237))
                self.table.item(self.table.currentRow(), n).setFont(QtGui.QFont(QtWidgets.QApplication.font().family(), italic=False))
            else:
                if int(self.table.item(self.table.currentRow(), 8).text()) == 1:
                    self.table.cellWidget(self.table.currentRow(), 0).setStyleSheet("background-color: rgb(224, 224, 224); color: rgb(204, 0, 0); font-style:italic")
                    self.table.item(self.table.currentRow(), n).setBackground(QtGui.QColor(224, 224, 224))
                    self.table.item(self.table.currentRow(), n).setForeground(QtGui.QColor(204, 0, 0))
                    self.table.item(self.table.currentRow(), n).setFont(QtGui.QFont(QtWidgets.QApplication.font().family(), italic=True))
                else:
                    self.table.cellWidget(self.table.currentRow(), 0).setStyleSheet('background-color: rgb(255, 255, 255)')
                    self.table.item(self.table.currentRow(), n).setBackground(QtGui.QColor(255, 255, 255))
                    self.table.item(self.table.currentRow(), n).setForeground(QtGui.QColor(0, 0, 0))
                    self.table.item(self.table.currentRow(), n).setFont(QtGui.QFont(QtWidgets.QApplication.font().family(), italic=False))


    def collect_data_from_table(self):
        self.updated_arh=[]
        arr = []
        for a in range(self.table.rowCount()):
            elem = self.table.cellWidget(a, 0)
            if elem.isChecked() == True:
                inner_item = []
                inner_item.append(self.table.cellWidget(a, 0).text())
                for b in range(1, self.table.columnCount()):
                    inner_item.append(self.table.item(a, b).text())
                arr.append(inner_item)
            else:
                pass
        for x in range(arr.__len__()):
            self.update_calculation(arr[x])

    def update_calculation(self, arr):
        if int(arr[8]) == 0:
            self.updated_arh.append(arr[0])
            from elements.mainGlobalObject import mainGlobalObject
            mainRecalcObj = mainGlobalObject()
            mainRecalcObj.city = arr[1]
            mainRecalcObj.object = arr[2]
            mainRecalcObj.location = arr[3]
            mainRecalcObj.position = arr[4]

            if int(arr[7]) == 2:
                mainRecalcObj.rto.proposal_ID = arr[0]
                get_eqiup_params('rto', mainRecalcObj)
                from widgets.rto_page.rtoWindow import RtoWindow
                RtoWindow.calculate_rto(self, get_all_params_rto(), mainRecalcObj)

        else:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setWindowTitle('Предупреждение')
            self.msg.setText(f'Предложение №{arr[0]} содержит ручные корректировки \n'
                             f'\nДанное предложение не может быть обновлено в автоматическом режиме.\n'
                             f'\nПопробуйте обновить его в ручном режиме.')
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.msg.show()

        self.confirm_update()

    def confirm_update(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle('Уведомление')

        text = 'Предложения с архивными номерами: \n'
        t2 = ''
        for x in range(self.updated_arh.__len__()):
            t2 += str(self.updated_arh[x])
            t2 += '\n'

        text += t2
        text += "успешно обновлены!"
        self.msg.setText(text)
        self.msg.show()
        self.msg.exec_()

# if __name__ == '__main__':
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     window = RecalculationItem()
#     window.show()
#     sys.exit(app.exec_())
