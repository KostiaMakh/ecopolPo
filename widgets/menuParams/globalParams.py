import qtawesome
from PyQt5 import QtWidgets, QtGui, uic, QtCore
from elements.sql.pushToCmbFromSql import getUniqFromColumn
from elements.sql.connectSql import connectToSql
from elements.sql.updateParamInSql import updateParamsInSQL
from elements.widgetsOperation.addPositionToCmb import addPositionToCMB


class GlobalParamsWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.connect = connectToSql()

        self.resize(800, 500)
        self.setWindowTitle('Редактор глобальны')
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.sqlTableName = "generalParam"
        self.sqlColumnName1 = "param_name"
        self.sqlColumnName2 = "param_value"
        self.sqlColumnName3 = "page"
        self.sqlColumnName4 = "cell"
        self.columnNameInWidget1 = "Параметр"
        self.columnNameInWidget2 = "Значение параметра"
        self.columnNameInWidget3 = "Страцица в расчете"
        self.columnNameInWidget4 = "Связанная ячейка"

        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.arhTable = QtWidgets.QTableWidget()
        self.arhTable.setWordWrap(True)
        self.arhTable.setColumnCount(4)
        self.arhTable.setColumnWidth(0, 200)
        self.arhTable.setColumnWidth(1, 150)
        self.arhTable.setColumnWidth(2, 150)
        self.arhTable.setColumnWidth(3, 150)

        self.butSend = QtWidgets.QPushButton('Обновить')
        self.butCancel = QtWidgets.QPushButton('Отменить')

        self.butCancel.clicked.connect(self.updateCancel)
        self.butSend.clicked.connect(self.sendUpdate)

        self.vbox.addWidget(self.arhTable)
        self.vbox.addWidget(self.butSend)
        self.vbox.addWidget(self.butCancel)

        self.widget.setLayout(self.vbox)
        self.setCentralWidget(self.widget)

        self.arhTable.setRowCount(30)
        self.arhTable.setHorizontalHeaderLabels([str(self.columnNameInWidget1),
                                                 str(self.columnNameInWidget2),
                                                 str(self.columnNameInWidget3),
                                                 str(self.columnNameInWidget4)])

        # Choose query content according to initial parameters
        query = f"""SELECT DISTINCT `{self.sqlColumnName1}`,
                                    `{self.sqlColumnName2}`,
                                    `{self.sqlColumnName3}`,
                                    `{self.sqlColumnName4}` FROM `{self.sqlTableName}`"""

        self.connect[1].execute(query)
        params = self.connect[1].fetchall()
        self.arhTable.setRowCount(len(params) + 20)

        for x in range(len(params)):
            self.arhTable.setItem(x, 0, QtWidgets.QTableWidgetItem(str(params[x][0])))
            self.arhTable.setItem(x, 1, QtWidgets.QTableWidgetItem(str(params[x][1])))
            self.arhTable.setItem(x, 2, QtWidgets.QTableWidgetItem(str(params[x][2])))
            self.arhTable.setItem(x, 3, QtWidgets.QTableWidgetItem(str(params[x][3])))

        self.arhTable.resizeRowsToContents()

    def updateCancel(self):
        self.close()

    def sendUpdate(self, parent):
        self.connect[0].ping()
        query = f"""TRUNCATE TABLE `{self.sqlTableName}`"""

        self.connect[1].execute(query)
        self.connect[0].commit()

        paramArr = []

        for x in range(self.arhTable.rowCount()):
            try:
                innerArr = []
                innerArr.append(self.arhTable.item(x, 0).text())
                innerArr.append(self.arhTable.item(x, 1).text())
                innerArr.append(self.arhTable.item(x, 2).text())
                innerArr.append(self.arhTable.item(x, 3).text())
                paramArr.append(innerArr)
            except:
                pass

        for x in range(len(paramArr)):
            try:
                query = f"""INSERT INTO `{self.sqlTableName}` (`{self.sqlColumnName1}`,
                                                                `{self.sqlColumnName2}`,
                                                                `{self.sqlColumnName3}`,
                                                                `{self.sqlColumnName4}`) VALUES (
                                                                '{str(paramArr[x][0])}',
                                                                '{str(paramArr[x][1])}',
                                                                '{str(paramArr[x][2])}',
                                                                '{str(paramArr[x][3])}')"""
                self.connect[1].execute(query)
                self.connect[0].commit()
            except:
                pass

        self.close()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = GlobalParamsWindow()
    window.show()
    sys.exit(app.exec_())
