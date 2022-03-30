from PyQt5 import QtWidgets, QtGui, QtCore, uic
from elements.sql.connectSql import connectToSql
from elements.sql.objectPageQuery import get_all_params, update_obj_params


class ObjParaWindow(QtWidgets.QMainWindow):
    def __init__(self,
                 parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        uic.loadUi('widgets\\objInf_w\\changeParams.ui', self)
        self.setWindowTitle('Редактор параметров вкладки')
        self.connect = connectToSql()
        all_params = get_all_params()

        # add managers from sql
        self.table_manager = QtWidgets.QTableWidget()
        self.table_manager.resize(590, 380)
        self.table_manager.setColumnCount(1)
        self.table_manager.setHorizontalHeaderLabels(['Менеджер'])
        self.table_manager.setColumnWidth(0, 200)
        self.table_manager.setRowCount(len(all_params[0]) + 10)

        self.add_items_into_table(table_name=self.table_manager,
                                  column_number=0,
                                  values_array=all_params[0])

        # add country from sql
        self.table_country = QtWidgets.QTableWidget()
        self.table_country.resize(590, 380)
        self.table_country.setColumnCount(1)
        self.table_country.setHorizontalHeaderLabels(['Страна'])
        self.table_country.setColumnWidth(0, 200)
        self.table_country.setRowCount(len(all_params[0]) + 10)

        self.add_items_into_table(table_name=self.table_country,
                                  column_number=0,
                                  values_array=all_params[1])

        self.stack_widget.addWidget(self.table_manager)
        self.stack_widget.addWidget(self.table_country)

        self.btn_manager.clicked.connect(lambda a: self.btn_param_clicked(0))
        self.btn_country.clicked.connect(lambda a: self.btn_param_clicked(1))

        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)

    def count_position_for_rows(self,
                                find_param,
                                find_column_count,
                                return_column_1,
                                return_column_2=None,
                                return_column_3=None):
        return_array_1 = []
        return_array_2 = []
        return_array_3 = []
        for x in range(len(self.sqlArhive)):
            if self.sqlArhive[x][int(find_column_count)] == str(find_param):
                return_array_1.append(self.sqlArhive[x][int(return_column_1)])
                try:
                    return_array_2.append(self.sqlArhive[x][int(return_column_2)])
                    return_array_3.append(self.sqlArhive[x][int(return_column_3)])
                except:
                    pass
            else:
                pass

        return [return_array_1, return_array_2, return_array_3]

    def add_items_into_table(self, table_name, column_number, values_array):
        for x in range(0, len(values_array)):
            table_name.setItem(x, int(column_number), QtWidgets.QTableWidgetItem(str(values_array[x][0])))

    def btn_param_clicked(self, caller):
        if caller == 0:
            marker = 0
        elif caller == 1:
            marker = 1
        elif caller == 2:
            marker = 2

        self.stack_widget.setCurrentIndex(int(marker))

    def btn_cancel_clicked(self):
        self.close()

    def btn_save_clicked(self):
        try:
            newParamsTable = []
            bufferArr = []

            # def adding sorted params in main arr
            def addFromBuffer(bArr):
                for a in range(len(bArr)):
                    newParamsTable.append(bArr[a])

                bArr.clear()

            # collect params values from table MANAGERS
            for x in range(self.table_manager.rowCount()):
                try:
                    if self.table_manager.item(x, 0).text() == '' \
                            or self.table_manager.item(x, 0).text() == 0:
                        raise Exception
                    else:
                        innerArr = []
                        innerArr.append('Менеджер')
                        innerArr.append(self.table_manager.item(x, 0).text())
                        bufferArr.append(innerArr)
                except:
                    pass

            bufferArr.sort(key=lambda a: str(a[1]))
            addFromBuffer(bufferArr)

            # collect params values from table COUNTRY
            for x in range(self.table_country.rowCount()):
                try:
                    if self.table_country.item(x, 0).text() == '' \
                            or self.table_country.item(x, 0).text() == 0:
                        raise Exception
                    else:
                        innerArr = []
                        innerArr.append('Страна')
                        innerArr.append(self.table_country.item(x, 0).text())
                        bufferArr.append(innerArr)
                except:
                    pass

            bufferArr.sort(key=lambda a: str(a[1]))
            addFromBuffer(bufferArr)

            update_obj_params(newParamsTable)

            from widgets.allerts.allerts import seccesfullUpdate
            seccesfullUpdate(self)

            self.close()

        except:
            from widgets.allerts.allerts import cantUpdateParamsInSql
            cantUpdateParamsInSql(self)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ObjParaWindow()
    window.show()
    sys.exit(app.exec_())
