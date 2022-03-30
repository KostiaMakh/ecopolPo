from PyQt5 import QtWidgets
import xlwings
import time
import os
from elements.mainGlobalObject import mainGlobalObject
from elements.sql.connectSql import connectToSql
from PyQt5 import QtWidgets

def manual_update_calculation(parent):
    def get_params_name_from_excel():
        params_name_arr = {}
        for x in range(1, 100):
            if wb.sheets['sql_update'].cells(x, 2).value is not None:
                params_name_arr[wb.sheets['sql_update'].cells(x, 2).value] = x
        return params_name_arr

    def find_param_in_excel(paramName):
        row_N = paramsName_Arr.get(paramName)
        return wb.sheets['sql_update'].cells(row_N, 3).value


    posArr = QtWidgets.QFileDialog.getOpenFileName(parent=parent, caption='Обновление предложения', filter="Excel (*.xlsx *xlsm)")
    if posArr[0] != '':
        connection = connectToSql()
        book_link = posArr[0].replace('/', '\\')
        wb = xlwings.Book(book_link)

        if int(wb.sheets['sql_update'].cells(1, 3).value) == 2:
            paramsName_Arr = get_params_name_from_excel()
            query = f'''UPDATE arhive, rto_arhive SET 
                arhive.city = '{find_param_in_excel('city')}', 
                arhive.object = '{find_param_in_excel('object')}', 
                arhive.location = '{find_param_in_excel('location')}', 
                arhive.position = '{find_param_in_excel('position')}', 
                arhive.mark = '{find_param_in_excel('mark')}', 
                arhive.menedger = '{find_param_in_excel('manager')}', 
                arhive.eqip_price = {int(find_param_in_excel('price'))}, 
                arhive.cp_price = {int(find_param_in_excel('controlPanel_price'))}, 
                arhive.weight = {int(find_param_in_excel('weight'))},
                arhive.ip = '{find_param_in_excel('driveIP')}', 
                arhive.power = {float(find_param_in_excel('power'))}, 
                arhive.material = '{find_param_in_excel('material')}',  
                arhive.date_ex = '{str(time.strftime("%d.%m.%Y %H:%M:%S"))}', 
                arhive.executer = '{str(os.getlogin())}', 
                arhive.description = '{str(find_param_in_excel('description_to_rdc'))}', 
                arhive.tkp_company = '{find_param_in_excel('company')}', 
                arhive.country = '{find_param_in_excel('country')}', 
                arhive.manualChange = {int(find_param_in_excel('manualChange'))}, 
                rto_arhive.gap = {int(find_param_in_excel('gap'))}, 
                rto_arhive.cw = {int(find_param_in_excel('channelWidth'))}, 
                rto_arhive.ch = {int(find_param_in_excel('channelDepth'))}, 
                rto_arhive.hUnload = {int(find_param_in_excel('unloadH'))}, 
                rto_arhive.cp = '{find_param_in_excel('controlPanel')}', 
                rto_arhive.protokol = '{find_param_in_excel('connection')}'   
                WHERE arhive.id = {int(find_param_in_excel('proposal_ID'))} AND rto_arhive.id = {int(find_param_in_excel('proposal_ID'))}'''

        connection[1].execute(query)
        connection[0].commit()
        wb.app.quit()

        return 1
    else:
        return 0





