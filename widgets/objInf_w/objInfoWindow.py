import qtawesome
from PyQt5 import QtWidgets, uic
from elements.sql.pushToCmbFromSql import getUniqFromColumn
from elements.sql.connectSql import connectToSql
from elements.widgetsOperation.addPositionToCmb import addPositionToCMB
from widgets.addToCmbW.addToCmbW import AddWindow
from elements.mainGlobalObject import mainGlobalObject
from widgets.objInf_w.changeParamObj import ObjParaWindow
from elements.sql.objectPageQuery import get_all_params
from widgets.menuParams.globalParams import GlobalParamsWindow
from elements.sql.objectPageQuery import get_all_params, update_obj_params
from elements.fileOperation.manualUpdateCalculation import manual_update_calculation

mainObj = mainGlobalObject()

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('widgets/objinf_w/objInfo.ui', self)
        self.connect = connectToSql()

        cities = getUniqFromColumn(self.connect[0],
                                   self.connect[1],
                                   tableName='arhive',
                                   columnName='city')
        addPositionToCMB(cities, self.cmb_city)
        self.cmb_city.setCurrentText('')

        self.cmb_city.currentTextChanged.connect(self.cityChange)
        self.cmb_object.currentTextChanged.connect(self.objectChange)

        self.btn_next.clicked.connect(self.butNextWindow)

        self.window_param.triggered.connect(self.changeParamWindow)
        self.mn_price_params.triggered.connect(self.change_price_params)
        self.update_data_in_sql.triggered.connect(lambda e: self.update_calculation_DB())
        self.inithial_filling()

    def inithial_filling(self):
        self.params_sql = get_all_params()
        try:
            self.cmb_manager.clear()
            self.cmb_country.clear()
        except: pass

        addPositionToCMB(self.params_sql[0], self.cmb_manager)
        addPositionToCMB(self.params_sql[1], self.cmb_country)

    def changeParamWindow(self):
        changePWindow = ObjParaWindow(self)
        changePWindow.show()

        # reanimate connection
        self.connect[0].ping()
        changePWindow.closeEvent = lambda e: self.inithial_filling()

    def change_price_params(self):
        w = GlobalParamsWindow(self)
        w.show()

    def cityChange(self):
        self.connect[0].ping()
        self.cmb_object.clear()
        # self.cmb_location.currentText()
        self.cmb_location.clear()
        # add objects
        objects = getUniqFromColumn(self.connect[0],
                                    self.connect[1],
                                    tableName='arhive',
                                    columnName='object',
                                    findParam=self.cmb_city.currentText(),
                                    findParamCategory='city')
        addPositionToCMB(objects, self.cmb_object)
        self.cmb_object.setCurrentText('')

    def objectChange(self):
        if self.cmb_object.currentText() != "":
            # self.cmb_location.currentText()
            self.cmb_location.clear()
            self.connect[0].ping()
            places = getUniqFromColumn(self.connect[0],
                                       self.connect[1],
                                       tableName='arhive',
                                       columnName='location',
                                       findParam=self.cmb_city.currentText(),
                                       findParamCategory='city',
                                       findParam2=self.cmb_object.currentText(),
                                       findParamCategory2='object')
            addPositionToCMB(places, self.cmb_location)
            self.cmb_location.setCurrentText('')
        else:
            pass

    def updateCmb(self, cmbModule, tableName, columnName):
        self.connect[0].ping()
        cmbModule.currentText()
        cmbModule.clear()
        params = getUniqFromColumn(self.connect[0],
                                   self.connect[1],
                                   tableName=tableName,
                                   columnName=columnName)
        addPositionToCMB(params, cmbModule)

    def butNextWindow(self):

        if self.comp_mp.isChecked():
            mainObj.company = self.comp_mp.text()
        elif self.comp_tpp.isChecked():
            mainObj.company = self.comp_tpp.text()
        elif self.comp_npf.isChecked():
            mainObj.company = self.comp_npf.text()

        mainObj.manager = self.cmb_manager.currentText()
        mainObj.client = self.cmb_customer.currentText()
        mainObj.country = self.cmb_country.currentText()
        mainObj.city = str(self.cmb_city.currentText())[0:10]
        mainObj.object = self.cmb_object.currentText()
        mainObj.location = self.cmb_location.currentText()
        mainObj.note = self.txt_note.toPlainText()

        from elements.widgetsOperation.analiseCmbFill import analiseCmbData

        mainObj.manager = analiseCmbData(mainObj.manager)
        mainObj.client = analiseCmbData(mainObj.client)
        mainObj.country = analiseCmbData(mainObj.country)
        mainObj.city = analiseCmbData(mainObj.city)
        mainObj.object = analiseCmbData(mainObj.object)
        mainObj.location = analiseCmbData(mainObj.location)

        from widgets.equipW.equipW import EquipW
        self.hide()

        nextW = EquipW(self)
        nextW.show()

    def update_calculation_DB(self):
        self.success_allert = QtWidgets.QMessageBox()
        self.success_allert.setWindowTitle('Обновление позиции в sql')

        a = manual_update_calculation(self)
        if a == 1:
            self.success_allert.setText('Предложение успешно обновлено')
            self.success_allert.setIcon(QtWidgets.QMessageBox.Information)
            self.success_allert.show()
        else:
            self.success_allert.setText('Не удалось обновить предложение')
            self.success_allert.setIcon(QtWidgets.QMessageBox.Critical)
            self.success_allert.show()


