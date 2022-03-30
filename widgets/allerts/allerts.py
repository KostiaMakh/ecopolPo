from PyQt5 import QtWidgets, QtGui, QtCore

def cantUpdateParamsInSql(parent):
    QtWidgets.QMessageBox.critical(parent, 'Ошибка', 'Не удалось обновить параметры \nПопробуйте ещё раз!',
                                   buttons=QtWidgets.QMessageBox.Close,
                                   defaultButton=QtWidgets.QMessageBox.Close)

def seccesfullUpdate(parent):
    QtWidgets.QMessageBox.information(parent, 'Сообщение', 'Данные успешно обновлены.\nПерезапустите страницу и проверьте правльность внесения данных!',
                                      buttons=QtWidgets.QMessageBox.Close,
                                      defaultButton=QtWidgets.QMessageBox.Close)
