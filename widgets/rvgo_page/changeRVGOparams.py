import qtawesome
from PyQt5 import QtWidgets, QtGui, uic, QtCore
from elements.sql.getsQuery import get_all_params_rvgo
from elements.sql.pushToCmbFromSql import getUniqFromColumn
from elements.sql.connectSql import connectToSql
from elements.sql.updateParamInSql import updateParamsInSQL
from elements.widgetsOperation.addPositionToCmb import addPositionToCMB
from elements.widgetsOperation.equipmetParams import add_items_into_table

sql_table_name = 'param_rvgo'


class ObjParamRVGOWindow(QtWidgets.QMainWindow):
    updateSignal = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.parent = parent
        self.cantMake = QtWidgets.QMessageBox()
        uic.loadUi('widgets\\rvgo_page\\changeParamsRVGO.ui', self)
        self.setWindowTitle('Редактор параметров вкладки')

        para_names_in_sql = ['Материал',
                             'Прозор, мм',
                             'Ширина канала, мм',
                             'Привод',
                             'Протокол',
                             'ШУ',
                             'Высота выгрузки, мм',
                             'Ссылка на ячейки',
                             'Ссылка на файл']

        self.sqlArhive = get_all_params_rvgo(para_names_in_sql)

        # add gaps from sql
        self.table_gap = QtWidgets.QTableWidget()
        self.table_gap.resize(590, 380)
        self.table_gap.setColumnCount(1)
        self.table_gap.setHorizontalHeaderLabels(['Прозор, мм'])
        self.table_gap.setColumnWidth(0, 200)

        self.table_gap.setRowCount(len(self.sqlArhive['Прозор, мм']) + 10)

        add_items_into_table(table_name=self.table_gap,
                             values_array=self.sqlArhive['Прозор, мм'])

        self.table_channel = QtWidgets.QTableWidget()
        self.table_channel.resize(590, 380)
        self.table_channel.setColumnCount(3)
        self.table_channel.setHorizontalHeaderLabels(
            ['Ширина канала, мм', 'Глубина канала (max), мм', 'Высота ф-го экрана (max), мм'])
        self.table_channel.setColumnWidth(0, 180)
        self.table_channel.setColumnWidth(1, 180)
        self.table_channel.setColumnWidth(2, 180)

        self.table_channel.setRowCount(len(self.sqlArhive['Ширина канала, мм']) + 10)

        add_items_into_table(table_name=self.table_channel,
                             values_array=self.sqlArhive['Ширина канала, мм'])

        self.table_hl = QtWidgets.QTableWidget()
        self.table_hl.resize(590, 380)
        self.table_hl.setColumnCount(1)
        self.table_hl.setHorizontalHeaderLabels(['Высота выгрузки, мм'])
        self.table_hl.setColumnWidth(0, 200)

        self.table_hl.setRowCount(len(self.sqlArhive['Высота выгрузки, мм']) + 10)

        add_items_into_table(table_name=self.table_hl,
                             values_array=self.sqlArhive['Высота выгрузки, мм'])

        self.table_driver = QtWidgets.QTableWidget()
        self.table_driver.resize(590, 380)
        self.table_driver.setColumnCount(1)
        self.table_driver.setHorizontalHeaderLabels(['IP привода'])
        self.table_driver.setColumnWidth(0, 200)

        self.table_driver.setRowCount(len(self.sqlArhive['Привод']) + 10)
        add_items_into_table(table_name=self.table_driver,
                                  values_array=self.sqlArhive['Привод'])

        self.table_cp = QtWidgets.QTableWidget()
        self.table_cp.resize(590, 380)
        self.table_cp.setColumnCount(1)
        self.table_cp.setHorizontalHeaderLabels(['Комплектный ШУ'])
        self.table_cp.setColumnWidth(0, 200)

        self.table_cp.setRowCount(len(self.sqlArhive['ШУ']) + 10)

        add_items_into_table(table_name=self.table_cp,
                             values_array=self.sqlArhive['ШУ'])

        self.table_protokol = QtWidgets.QTableWidget()
        self.table_protokol.resize(590, 380)
        self.table_protokol.setColumnCount(1)
        self.table_protokol.setHorizontalHeaderLabels(['Протокол связи'])
        self.table_protokol.setColumnWidth(0, 200)

        self.table_protokol.setRowCount(len(self.sqlArhive['Протокол']) + 10)

        add_items_into_table(table_name=self.table_protokol,
                             values_array=self.sqlArhive['Протокол'])

        self.table_mat = QtWidgets.QTableWidget()
        self.table_mat.resize(590, 380)
        self.table_mat.setColumnCount(1)
        self.table_mat.setHorizontalHeaderLabels(['Материал исполнения'])
        self.table_mat.setColumnWidth(0, 200)

        self.table_mat.setRowCount(len(self.sqlArhive['Материал']) + 10)

        add_items_into_table(table_name=self.table_mat,
                             values_array=self.sqlArhive['Материал'])

        self.table_cell_links = QtWidgets.QTableWidget()
        self.table_cell_links.resize(590, 380)
        self.table_cell_links.setColumnCount(2)
        self.table_cell_links.setHorizontalHeaderLabels(['Страница', 'Ячейка'])
        self.table_cell_links.setColumnWidth(0, 160)
        self.table_cell_links.setColumnWidth(1, 160)
        self.table_cell_links.verticalHeader().setFixedWidth(180)


        self.table_cell_links.setRowCount(len(self.sqlArhive['Ссылка на ячейки']))

        add_items_into_table(table_name=self.table_cell_links,
                             values_array=self.sqlArhive['Ссылка на ячейки'],
                             vertical_headers_number=True)

        self.table_book_links = QtWidgets.QTableWidget()
        self.table_book_links.resize(590, 380)
        self.table_book_links.setColumnCount(1)
        self.table_book_links.setHorizontalHeaderLabels(['Ссылка на файл'])
        self.table_book_links.setColumnWidth(0, 350)
        self.table_book_links.verticalHeader().setFixedWidth(150)

        self.table_book_links.setRowCount(len(self.sqlArhive['Ссылка на файл']))

        add_items_into_table(table_name=self.table_book_links,
                             values_array=self.sqlArhive['Ссылка на файл'],
                             vertical_headers_number=True)
        #
        self.stack_widget.addWidget(self.table_gap)
        self.stack_widget.addWidget(self.table_channel)
        self.stack_widget.addWidget(self.table_hl)
        self.stack_widget.addWidget(self.table_driver)
        self.stack_widget.addWidget(self.table_cp)
        self.stack_widget.addWidget(self.table_protokol)
        self.stack_widget.addWidget(self.table_mat)
        self.stack_widget.addWidget(self.table_cell_links)
        self.stack_widget.addWidget(self.table_book_links)

        self.btn_gap.clicked.connect(lambda a: self.btn_param_clicked(0))
        self.btn_chanel.clicked.connect(lambda a: self.btn_param_clicked(1))
        self.btn_hl.clicked.connect(lambda a: self.btn_param_clicked(2))
        self.btn_driver.clicked.connect(lambda a: self.btn_param_clicked(3))
        self.btn_cp.clicked.connect(lambda a: self.btn_param_clicked(4))
        self.btn_protokol.clicked.connect(lambda a: self.btn_param_clicked(5))
        self.btn_mat.clicked.connect(lambda a: self.btn_param_clicked(6))
        self.btn_cell_links.clicked.connect(lambda a: self.btn_param_clicked(7))
        self.btn_book_links.clicked.connect(lambda a: self.btn_param_clicked(8))

        # self.control = 1
        # # control param
        # # 1 - managers
        # # 2 - country
        #
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)


    def btn_param_clicked(self, caller):
        if caller == 0:
            marker = 0
        elif caller == 1:
            marker = 1
        elif caller == 2:
            marker = 2
        elif caller == 3:
            marker = 3
        elif caller == 4:
            marker = 4
        elif caller == 5:
            marker = 5
        elif caller == 6:
            marker = 6
        elif caller == 7:
            marker = 7
        elif caller == 8:
            marker = 8

        self.stack_widget.setCurrentIndex(int(marker))

    def btn_cancel_clicked(self):
        self.close()

    def collect_new_params_from_tables(self):
        newParmsTable = []
        bufferArr = []

            # def adding sorted params in main arr
        def addFromBuffer(bArr):
            for a in range(len(bArr)):
                newParmsTable.append(bArr[a])
            bArr.clear()

        # collect params values from table. GAP
        for x in range(self.table_gap.rowCount()):
            try:
                if self.table_gap.item(x, 0).text() == '' \
                        or self.table_gap.item(x, 0).text() == 0 \
                        or int(self.table_gap.item(x, 0).text()) == False:
                    raise Exception
                else:
                    innerArr = []
                    innerArr.append('Прозор, мм')
                    innerArr.append(self.table_gap.item(x, 0).text())
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    bufferArr.append(innerArr)
            except:
                pass

        bufferArr.sort(key=lambda a: int(a[1]))
        addFromBuffer(bufferArr)

        # collect params values from table. CHANNEL
        for x in range(self.table_channel.rowCount()):
            try:
                if self.table_channel.item(x, 0).text() == '' or \
                        self.table_channel.item(x, 0).text() == 0 or \
                        int(self.table_channel.item(x, 0).text()) == False or \
                        self.table_channel.item(x, 1).text() == '' or \
                        self.table_channel.item(x, 1).text() == 0 or \
                        int(self.table_channel.item(x, 1).text()) == False or \
                        self.table_channel.item(x, 2).text() == '' or \
                        self.table_channel.item(x, 2).text() == 0 or \
                        int(self.table_channel.item(x, 2).text()) == False:
                    raise Exception
                else:
                    innerArr = []
                    innerArr.append('Ширина канала, мм')
                    innerArr.append(self.table_channel.item(x, 0).text())
                    innerArr.append(self.table_channel.item(x, 1).text())
                    innerArr.append(self.table_channel.item(x, 2).text())
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    bufferArr.append(innerArr)
            except:
                pass

        bufferArr.sort(key=lambda a: int(a[1]))
        addFromBuffer(bufferArr)

        # collect params values from table. H UNLOAD
        for x in range(self.table_hl.rowCount()):
            try:
                if self.table_hl.item(x, 0).text() == '' or self.table_hl.item(x, 0).text() == 0 or int(
                        self.table_hl.item(x, 0).text()) == False:
                    raise Exception
                else:
                    innerArr = []
                    innerArr.append('Высота выгрузки, мм')
                    innerArr.append(self.table_hl.item(x, 0).text())
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    bufferArr.append(innerArr)
            except:
                pass

        bufferArr.sort(key=lambda a: int(a[1]))
        addFromBuffer(bufferArr)

        # collect params values from table. DRIVE IP
        for x in range(self.table_driver.rowCount()):
            try:
                if self.table_driver.item(x, 0).text() == '' or self.table_driver.item(x, 0).text() == 0 or int(
                        self.table_driver.item(x, 0).text()) == False:
                    raise Exception
                else:
                    innerArr = []
                    innerArr.append('Привод')
                    innerArr.append(self.table_driver.item(x, 0).text())
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    bufferArr.append(innerArr)
            except:
                pass

        bufferArr.sort(key=lambda a: int(a[1]))
        addFromBuffer(bufferArr)

        # collect params values from table. CP COMPLECTATION
        for x in range(self.table_cp.rowCount()):
            try:
                if self.table_cp.item(x, 0).text() == '' or self.table_cp.item(x, 0).text() == 0:
                    raise Exception
                else:
                    innerArr = []
                    innerArr.append('ШУ')
                    innerArr.append(self.table_cp.item(x, 0).text())
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    bufferArr.append(innerArr)
            except:
                pass

        bufferArr.sort(key=lambda a: str(a[1]))
        addFromBuffer(bufferArr)

        # collect params values from table. CP CONNECTION PROTOCOL
        for x in range(self.table_protokol.rowCount()):
            try:
                if self.table_protokol.item(x, 0).text() == '' or self.table_protokol.item(x, 0).text() == 0:
                    raise Exception
                else:
                    innerArr = []
                    innerArr.append('Протокол')
                    innerArr.append(self.table_protokol.item(x, 0).text())
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    bufferArr.append(innerArr)
            except:
                pass

        bufferArr.sort(key=lambda a: str(a[1]))
        addFromBuffer(bufferArr)

        # collect params values from table. MATERIALS
        for x in range(self.table_mat.rowCount()):
            try:
                if self.table_mat.item(x, 0).text() == '' or self.table_mat.item(x, 0).text() == 0:
                    raise Exception
                else:
                    innerArr = []
                    innerArr.append('Материал')
                    innerArr.append(self.table_mat.item(x, 0).text())
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    bufferArr.append(innerArr)
            except:
                pass

        bufferArr.sort(key=lambda a: str(a[1]))
        addFromBuffer(bufferArr)

        # collect params values from table. CELLS LINKS
        for x in range(self.table_cell_links.rowCount()):
            try:
                if self.table_cell_links.item(x, 0).text() == '' or \
                        self.table_cell_links.item(x, 0).text() == 0 or \
                        self.table_cell_links.item(x, 1).text() == '' or \
                        self.table_cell_links.item(x, 1).text() == 0:

                    raise Exception
                else:
                    innerArr = []
                    innerArr.append('Ссылка на ячейки')
                    innerArr.append(self.table_cell_links.verticalHeaderItem(x).text())
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append(self.table_cell_links.item(x, 0).text())
                    innerArr.append(self.table_cell_links.item(x, 1).text())
                    innerArr.append('')
                    bufferArr.append(innerArr)
            except:
                pass

        bufferArr.sort(key=lambda a: str(a[4]))
        addFromBuffer(bufferArr)

        # collect params values from table. CELLS LINKS
        for x in range(self.table_book_links.rowCount()):
            try:
                if self.table_book_links.item(x, 0).text() == '' or \
                        self.table_book_links.item(x, 0).text() == 0:
                    raise Exception
                else:
                    innerArr = []
                    innerArr.append('Ссылка на файл')
                    innerArr.append(self.table_book_links.verticalHeaderItem(x).text())
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append('')
                    innerArr.append(self.table_book_links.item(x, 0).text())
                    bufferArr.append(innerArr)
            except:
                pass

        bufferArr.sort(key=lambda a: str(a[1]))
        addFromBuffer(bufferArr)

        return newParmsTable

    def push_new_params_in_sql(self, paramsArr):
        self.connect = connectToSql()
        query = f"""TRUNCATE TABLE `{sql_table_name}`"""
        self.connect[0].ping()
        self.connect[1].execute(query)
        self.connect[0].commit()

        query = f"""INSERT INTO `{sql_table_name}` (`param_name`, `val_1`, `min`, `max`, `sheet`, `cell`, `link`) VALUES """
        for x in range(0, len(paramsArr)):
            qr = f"""('{paramsArr[x][0]}','{paramsArr[x][1]}','{paramsArr[x][2]}','{paramsArr[x][3]}','{paramsArr[x][4]}','{paramsArr[x][5]}','{paramsArr[x][6]}'), """
            query = query + qr
        query = query[:-2]

        self.connect[0].ping()
        self.connect[1].execute(query)
        self.connect[0].commit()

    def btn_save_clicked(self):
        try:
            # 1. collect new params from table in new array (collect_new_params_from_tables)
            # 2. transfer this array for query creating and pushing into sql in function "push_new_params_in_sql"
            self.push_new_params_in_sql(self.collect_new_params_from_tables())

            from widgets.allerts.allerts import seccesfullUpdate
            seccesfullUpdate(self)

            self.updateSignal.emit(1)

            self.close()

        except:
            from widgets.allerts.allerts import cantUpdateParamsInSql
            cantUpdateParamsInSql(self)


# if __name__ == '__main__':
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     window = ObjParamRTOWindow()
#     window.show()
#     sys.exit(app.exec_())
