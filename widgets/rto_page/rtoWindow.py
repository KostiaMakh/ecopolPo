from PyQt5 import QtWidgets, QtGui, QtCore, uic
import PyQt5
import xlwings
import time
from elements.sql.addNewPosition import addNewPositionToArhive, addProposalNameToArhive
from elements.sql.equip_arhive import addNewPosition_RTO_ToArhive
from elements.sql.getsQuery import get_all_params_rto, get_all_params_rto2
from widgets.objInf_w.objInfoWindow import mainObj
from elements.sql.connectSql import connectToSql
from elements.sql.pushToCmbFromSql import getUniqFromColumn
from elements.widgetsOperation.addPositionToCmb import addPositionToCMB
from widgets.rto_page.changeRTOparams import ObjParamRTOWindow
from widgets.reCalcuateItem.reCalcItem import RecalculationItem
from widgets.menuParams.globalParams import GlobalParamsWindow
from elements.fileOperation.manualUpdateCalculation import manual_update_calculation

class RtoWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.connect = connectToSql()
        self.parent = parent
        uic.loadUi("widgets/rto_page/rto_window.ui", self)

        self.pix = QtGui.QPixmap('img/РГО_РТО.jpg')
        self.lb_img.setPixmap(self.pix)

        self.btn_back.clicked.connect(self.back_page)
        self.btn_calculate.clicked.connect(self.calculate)

        self.allParamsPTO = get_all_params_rto()

        positions = getUniqFromColumn(self.connect[0],
                                      self.connect[1],
                                      tableName='arhive',
                                      columnName='position',
                                      findParam=mainObj.city,
                                      findParamCategory='city',
                                      findParam2=mainObj.location,
                                      findParamCategory2='location')
        addPositionToCMB(positions, self.cmb_position)
        self.cmb_position.setCurrentText('')

        self.mn_globalParams.triggered.connect(self.change_global_params)
        self.menu_bth_renew.triggered.connect(self.renew_position)
        self.mn_price_params.triggered.connect(self.change_price_params)
        # self.update_data_in_sql.triggered.connect(lambda e: manual_update_calculation(self))

        self.initial_cmb_filling()

        self.cmb_cw.currentTextChanged.connect(self.change_cw)
        self.cmb_cp.currentTextChanged.connect(self.cp_change)

    def initial_cmb_filling(self):

        para_names_in_sql = ['Материал',
                             'Прозор, мм',
                             'Ширина канала, мм',
                             'Привод',
                             'Протокол',
                             'ШУ',
                             'Высота выгрузки, мм',
                             'Ссылка на ячейки',
                             'Ссылка на файл']

        self.allParams = get_all_params_rto2(para_names_in_sql)


        # self.allParamsPTO = get_all_params_rto()
        try:
            self.cmb_gap.clear()
            self.cmb_mat.clear()
            self.cmb_cw.clear()
            self.cmb_ip.clear()
            self.cmb_cp.clear()
            self.cmb_hl.clear()
        except:
            pass

        addPositionToCMB(self.allParams['Прозор, мм'], self.cmb_gap)
        addPositionToCMB(self.allParams['Материал'], self.cmb_mat)

        channelWidth = []
        for x in range(self.allParams['Ширина канала, мм'].__len__()):
            channelWidth.append(self.allParams['Ширина канала, мм'][x][0])

        addPositionToCMB(channelWidth, self.cmb_cw)

        # channelWidth = []
        # for x in range(self.allParamsPTO[2].__len__()):
        #     channelWidth.append(self.allParamsPTO[2][x][0])

        # addPositionToCMB(channelWidth, self.cmb_cw)
        addPositionToCMB(self.allParams['Привод'], self.cmb_ip)
        addPositionToCMB(self.allParams['ШУ'], self.cmb_cp)
        addPositionToCMB(self.allParams['Высота выгрузки, мм'], self.cmb_hl)

        self.cp_change()
        self.change_cw()

    def cp_change(self):
        if self.cmb_cp.currentText() == "Нет":
            self.cmb_protokol.clear()
            self.cmb_protokol.addItem("Нет")
            self.cmb_protokol.setEnabled(False)

        else:
            self.cmb_protokol.clear()
            addPositionToCMB(self.allParamsPTO[5], self.cmb_protokol)
            self.cmb_protokol.setEnabled(True)

    def back_page(self):
        self.hide()
        self.parent.show()

    def change_cw(self):
        try:
            self.cmb_ch.clear()

            # get channel parameters from arhive `self.allParamsPTO`
            channelw_d = []
            for x in range(self.allParams['Ширина канала, мм'].__len__()):
                if int(self.allParams['Ширина канала, мм'][x][0]) == int(self.cmb_cw.currentText()):
                    channelw_d.append(self.allParams['Ширина канала, мм'][x][1])
                    channelw_d.append(self.allParams['Ширина канала, мм'][x][2])
                else:
                    pass
            # create new array of channels dept for `cmb_cw.currentText()`
            channel_depth = []
            for ix in range(int(channelw_d[0]), int(channelw_d[1]), 100):
                channel_depth.append(ix)

            # add array with channel depth int to `self.cmb_c`
            addPositionToCMB(channel_depth, self.cmb_ch)

        except:
            pass

    def renew_position(self):
        r = RecalculationItem(self)
        r.show()

    def change_price_params(self):
        w = GlobalParamsWindow(self)
        w.show()

    def change_global_params(self):
        w = ObjParamRTOWindow(self)
        w.show()
        w.updateSignal.connect(self.initial_cmb_filling)

    def calculate(self):
        mainObj.rto.gap = self.cmb_gap.currentText()
        mainObj.rto.channelWidth = self.cmb_cw.currentText()
        mainObj.rto.channelDepth = self.cmb_ch.currentText()
        mainObj.rto.unloadH = self.cmb_hl.currentText()
        mainObj.rto.driveIP = self.cmb_ip.currentText()
        mainObj.rto.material = self.cmb_mat.currentText()
        mainObj.rto.controlPanel = self.cmb_cp.currentText()
        mainObj.rto.connection = self.cmb_protokol.currentText()
        mainObj.position = self.cmb_position.currentText()

        self.calculate_rto(self.allParamsPTO, mainObj)

    def calculate_rto(self, paramsArr, mainObj):
        import xlwings
        import time

        def add_value_in_excel_cell(linksArr, findParam, value):
            for x in (range(linksArr.__len__())):
                if linksArr[x][0] == findParam:
                    wb.sheets[str(f'{linksArr[x][1]}')].range(f'{linksArr[x][2]}').value = value


        wb = xlwings.Book(str(paramsArr[8][0][1]).replace('/', '\\'))

        from elements.fileOperation.pushGepParamToCalculation import pushParamsToFile
        pushParamsToFile(xlWorkBook=wb)

        add_value_in_excel_cell(paramsArr[7], 'Материал', mainObj.rto.material)
        add_value_in_excel_cell(paramsArr[7], 'Ширина канала', mainObj.rto.channelWidth)
        add_value_in_excel_cell(paramsArr[7], 'Прозор', mainObj.rto.gap)
        add_value_in_excel_cell(paramsArr[7], 'Глубина канала', mainObj.rto.channelDepth)
        add_value_in_excel_cell(paramsArr[7], 'Высота выгрузки', mainObj.rto.unloadH)
        add_value_in_excel_cell(paramsArr[7], 'Привод', mainObj.rto.driveIP)
        add_value_in_excel_cell(paramsArr[7], 'ШУ', mainObj.rto.controlPanel)
        add_value_in_excel_cell(paramsArr[7], 'Протокол', mainObj.rto.connection)

        add_value_in_excel_cell(paramsArr[7], 'Дата', time.strftime("%d.%m.%Y"))
        add_value_in_excel_cell(paramsArr[7], 'Менеджер', mainObj.manager)
        add_value_in_excel_cell(paramsArr[7], 'Страна', mainObj.country)
        add_value_in_excel_cell(paramsArr[7], 'Город', mainObj.city)
        add_value_in_excel_cell(paramsArr[7], 'Объект', mainObj.object)
        add_value_in_excel_cell(paramsArr[7], 'Место установки', mainObj.location)
        add_value_in_excel_cell(paramsArr[7], 'Позиция по проекту', mainObj.position)
        add_value_in_excel_cell(paramsArr[7], 'Страна', mainObj.country)
        add_value_in_excel_cell(paramsArr[7], 'Блан организации', mainObj.company)

        # get information from calculation
        mainObj.rto.weight = wb.sheets['Спецификация'].range('D36').value
        mainObj.rto.mark = wb.sheets['Спецификация'].range('D23').value
        mainObj.rto.power = wb.sheets['Спецификация'].range('D35').value
        mainObj.rto.price = wb.sheets['Спецификация'].range('C101').value
        mainObj.rto.controlPanel_price = wb.sheets['Спецификация'].range('D101').value

        mainObj.rto.description_to_rdc = wb.sheets['Цена'].range('I5').value

        mainObj.rto.proposal_ID = addNewPositionToArhive(city=mainObj.city,
                                                         object=mainObj.object,
                                                         location=mainObj.location,
                                                         position=mainObj.position,
                                                         mark=mainObj.rto.mark,
                                                         manager=mainObj.manager,
                                                         equip_price=mainObj.rto.price,
                                                         cp_price=mainObj.rto.controlPanel_price,
                                                         weight=mainObj.rto.weight,
                                                         ip=str(f'IP {mainObj.rto.driveIP}'),
                                                         power=mainObj.rto.power,
                                                         material=mainObj.rto.material,
                                                         executor=mainObj.user,
                                                         equip_code=mainObj.rto.equipDescription_code,
                                                         description=mainObj.rto.description_to_rdc,
                                                         country=mainObj.country,
                                                         tkp_company=mainObj.company)

        mainObj.rto.name_proposal = str('ТКП №' + str(mainObj.rto.proposal_ID) + ' '\
                                        + str(mainObj.city) + ' '\
                                        + str(mainObj.object) + ' '\
                                        + str(time.strftime("%d.%m.%Y")))

        add_value_in_excel_cell(paramsArr[7], 'Номер предложения', mainObj.rto.proposal_ID)
        # wb.sheets['Цена'].range('B9').value = mainObj.rto.proposal_ID
        #
        mainObj.rto.name_calculation = wb.sheets['Цена'].range('I3').value
        #
        addProposalNameToArhive(int(mainObj.rto.proposal_ID), "ТКП №" + str(mainObj.rto.name_calculation) + ".doc")
        #
        addNewPosition_RTO_ToArhive(mainObj)
        #
        from elements.fileOperation.proposal_forming import create_proposal
        create_proposal(calculationFile=wb,
                        proposalSample=str(paramsArr[8][1][1]).replace('/', '\\'),
                        proposalSavingDirectory="D:\\1_newProgram(ver.2)\\docs\\proposals",
                        fileName=mainObj.rto.name_proposal)

        wb.save(f'D:\\1_newProgram(ver.2)\\docs\\initial\\{str(mainObj.rto.name_calculation)}.xlsx')
        #
        wb.app.quit()


