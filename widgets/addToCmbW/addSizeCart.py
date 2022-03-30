from PyQt5 import QtWidgets, QtGui, uic, QtCore
from elements.sql.connectSql import connectToSql


class AddWindowChanelParameters(QtWidgets.QMainWindow):
    def __init__(self,
                 parent=None,
                 windowTitle=None,
                 sqlTableName=None,
                 tableColumnName1=None,
                 tableColumnName2=None,
                 tableColumnName3=None,
                 sqlColumnName0=None,
                 sqlColumnName1=None,
                 sqlColumnName2=None,
                 sqlColumnName3=None,
                 findParam0=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.parent = parent
        self.windowTitle = windowTitle
        self.sqlTableName = sqlTableName
        self.tableColumnName1 = tableColumnName1
        self.tableColumnName2 = tableColumnName2
        self.tableColumnName3 = tableColumnName3
        self.sqlColumnName0 = sqlColumnName0
        self.sqlColumnName1 = sqlColumnName1
        self.sqlColumnName2 = sqlColumnName2
        self.sqlColumnName3 = sqlColumnName3
        self.findParam0 = findParam0

        query = f"""SELECT DISTINCT `{self.sqlColumnName1}`, `{self.sqlColumnName2}`, `{self.sqlColumnName3}` FROM `{self.sqlTableName}` WHERE `{self.sqlColumnName0}`='{self.findParam0}'"""
        print(query)

        self.conn = connectToSql()
        self.connection = self.conn[0]
        self.cursor = self.conn[1]

        self.resize(700, 500)
        self.setWindowTitle(str(self.windowTitle))
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.sqlTableName = self.sqlTableName

        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.arhTable = QtWidgets.QTableWidget()
        self.arhTable.setColumnCount(3)
        self.arhTable.setColumnWidth(0, 150)
        self.arhTable.setColumnWidth(1, 230)
        self.arhTable.setColumnWidth(2, 230)

        self.butSend = QtWidgets.QPushButton('Обновить')
        self.butCancel = QtWidgets.QPushButton('Отменить')

        self.butCancel.clicked.connect(self.updateCancel)
        self.butSend.clicked.connect(self.sendUpdate)

        self.vbox.addWidget(self.arhTable)
        self.vbox.addWidget(self.butSend)
        self.vbox.addWidget(self.butCancel)

        self.widget.setLayout(self.vbox)
        self.setCentralWidget(self.widget)

        self.arhTable.setHorizontalHeaderLabels([str(self.tableColumnName1),
                                                 str(self.tableColumnName2),
                                                 str(self.tableColumnName3)])

        query = f"""SELECT DISTINCT `{self.sqlColumnName1}`, `{self.sqlColumnName2}`, `{self.sqlColumnName3}` FROM `{self.sqlTableName}` WHERE `{self.sqlColumnName0}`='{self.findParam0}'"""
        print(query)

        self.cursor.execute(query)
        params = self.cursor.fetchall()

        self.arhTable.setRowCount(int(len(params)+20))

        for x in range(len(params)):
            self.arhTable.setItem(x, 0, QtWidgets.QTableWidgetItem(str(params[x][0])))
            self.arhTable.setItem(x, 1, QtWidgets.QTableWidgetItem(str(params[x][1])))
            self.arhTable.setItem(x, 2, QtWidgets.QTableWidgetItem(str(params[x][2])))


    def sendUpdate(self, parent):
        self.connection.ping()
        query = f"""DELETE FROM `{self.sqlTableName}` WHERE `{self.sqlColumnName0}`='{self.findParam0}'"""
        self.cursor.execute(query)
        self.connection.commit()

        params = []
        for m in range(int(self.arhTable.rowCount())):
            try:
                if self.arhTable.item(m, 0).text() == '':
                    pass
                else:
                    query = f"""INSERT INTO `{self.sqlTableName}` (`{self.sqlColumnName0}`, `{self.sqlColumnName1}`, `{self.sqlColumnName2}`, `{self.sqlColumnName3}`) VALUES 
                    ('{self.findParam0}', '{self.arhTable.item(m, 0).text()}', {int(self.arhTable.item(m, 1).text())}, {self.arhTable.item(m, 2).text()})"""

                    self.cursor.execute(query)
                    self.connection.commit()

                    # innerArr = []
                    # innerArr.append(self.arhTable.item(m, 0).text())
                    # innerArr.append(self.arhTable.item(m, 1).text())
                    # innerArr.append(self.arhTable.item(m, 2).text())
                    # params.append(innerArr)
                    # print(params)
            except: pass

        # print(params)

        self.close()

    def updateCancel(self):
        self.close()


