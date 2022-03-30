import qtawesome
from PyQt5 import QtWidgets, QtGui, uic, QtCore
from elements.sql.pushToCmbFromSql import getUniqFromColumn
from elements.sql.connectSql import connectToSql
from elements.sql.updateParamInSql import updateParamsInSQL
from elements.widgetsOperation.addPositionToCmb import addPositionToCMB


class AddWindow(QtWidgets.QMainWindow):
    def __init__(self,
                 parent=None,
                 windowTitle=None,
                 sqlTableName=None,
                 sqlColumnName=None,
                 columnNameInWidget=None,
                 findParam=None,
                 findParamCategory=None,
                 findParam2=None,
                 findParamCategory2=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        # uic.loadUi('widgets/addToCmbW/optionWtable.ui', self)
        self.connect = connectToSql()

        self.resize(400, 500)
        self.setWindowTitle(str(windowTitle))
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.sqlTableName = sqlTableName
        self.sqlColumnName = sqlColumnName
        self.findParam = findParam
        self.findParamCategory = findParamCategory
        self.findParam2 = findParam2
        self.findParamCategory2 = findParamCategory2

        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.arhTable = QtWidgets.QTableWidget()
        self.arhTable.setColumnCount(2)
        self.arhTable.setColumnWidth(0, 200)

        self.butSend = QtWidgets.QPushButton('Обновить')
        self.butCancel = QtWidgets.QPushButton('Отменить')

        self.butCancel.clicked.connect(self.updateCancel)
        self.butSend.clicked.connect(self.sendUpdate)

        self.vbox.addWidget(self.arhTable)
        self.vbox.addWidget(self.butSend)
        self.vbox.addWidget(self.butCancel)

        self.widget.setLayout(self.vbox)
        self.setCentralWidget(self.widget)

        self.arhTable.setColumnCount(1)
        self.arhTable.setRowCount(30)
        self.arhTable.setHorizontalHeaderLabels([str(columnNameInWidget)])

        # Choose query content according to initial parameters
        if self.findParam is None and self.findParam2 is None:
            params = getUniqFromColumn(self.connect[0],
                                    self.connect[1],
                                    tableName=self.sqlTableName,
                                    columnName=self.sqlColumnName)
        elif self.findParam is not None and self.findParam2 is None:
            params = getUniqFromColumn(self.connect[0],
                                    self.connect[1],
                                    tableName=self.sqlTableName,
                                    columnName=self.sqlColumnName,
                                    findParam=self.findParam,
                                    findParamCategory=self.findParamCategory)
        else:
            params = getUniqFromColumn(self.connect[0],
                                    self.connect[1],
                                    tableName=self.sqlTableName,
                                    columnName=self.sqlColumnName,
                                    findParam=self.findParam,
                                    findParamCategory=self.findParamCategory,
                                    findParam2=self.findParam2,
                                    findParamCategory2=self.findParamCategory2)
        self.arhTable.setRowCount(len(params) + 20)

        for x in range(len(params)):
            self.arhTable.setItem(x, 0, QtWidgets.QTableWidgetItem(str(params[x])))


    def updateCancel(self):
        self.close()

    def sendUpdate(self, parent):
        params = []
        for m in range(int(self.arhTable.rowCount())):
            try:
                if self.arhTable.item(m, 0).text() == '':
                    pass
                else:
                    # if self.arhTable.item(m, 0) != '':
                    params.append(self.arhTable.item(m, 0).text())
                    print(params)
            except: pass

        print(params)

        self.connect[0].ping()
        updateParamsInSQL(self.connect[0],
                          self.connect[1],
                          tableName=self.sqlTableName,
                          columnName=self.findParamCategory,
                          columnName1=self.sqlColumnName,
                          paramsArray=params,
                          findParam=self.findParam
                          )
        self.close()

