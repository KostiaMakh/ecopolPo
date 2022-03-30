from elements.sql.connectSql import connectToSql

rtoTableInSql = 'param_rto'

def get_all_params_rto():
    con = connectToSql()
    connection = con[0]
    cursor = con[1]

    query = f"""SELECT * FROM `{rtoTableInSql}`"""

    cursor.execute(query)
    params_arh = cursor.fetchall()

    para_names_in_sql = {0: 'Материал',
                         1: 'Прозор, мм',
                         2: 'Ширина канала, мм',
                         3: 'Привод',
                         4: 'Протокол',
                         5: 'ШУ',
                         6: 'Высота выгрузки, мм',
                         7: 'Ссылка на ячейки',
                         8: 'Ссылка на файл'}

    def _filerParams(paramsID):
        array = []
        for x in range(len(params_arh)):
            if params_arh[x][0] == para_names_in_sql[paramsID]:
                innerArr = []
                for a in range(1, len(params_arh[x])):
                    if params_arh[x][a] is None or params_arh[x][a] == '' or params_arh[x][a] == 0:
                        pass
                    else:
                        innerArr.append(params_arh[x][a])
                array.append(innerArr)
        return array


    gaps = _filerParams(1)
    material = _filerParams(0)
    channels = _filerParams(2)
    driveIP = _filerParams(3)
    controlPanel = _filerParams(5)
    cpProtocol = _filerParams(4)
    unloadHeight = _filerParams(6)
    bookCells = _filerParams(7)
    filesLinks = _filerParams(8)

    return [gaps, material, channels, driveIP, controlPanel, cpProtocol, unloadHeight, bookCells, filesLinks]

def get_all_params_erpe(param_names_in_sql):
    return _getAllParamsFromSql('param_erpe', param_names_in_sql)

def get_all_params_rvgo(param_names_in_sql):
    return _getAllParamsFromSql('param_rvgo', param_names_in_sql)

def get_all_params_rto2(para_names_in_sql):
    return _getAllParamsFromSql('param_rto', para_names_in_sql)

def _getAllParamsFromSql(sqlTableName, paramsNamesArray):

    def _filerParams(paramsID):
        array = []
        for x in range(len(params_arh)):
            if params_arh[x][0] == paramsID:
                innerArr = []
                for a in range(1, len(params_arh[x])):
                    if params_arh[x][a] is None or params_arh[x][a] == '' or params_arh[x][a] == 0:
                        pass
                    else:
                        innerArr.append(params_arh[x][a])
                array.append(innerArr)
        return array

    con = connectToSql()
    connection = con[0]
    cursor = con[1]
    query = f"""SELECT * FROM `{sqlTableName}`"""
    cursor.execute(query)
    params_arh = cursor.fetchall()

    paramsTuple = {}
    for x in range(paramsNamesArray.__len__()):
        m = paramsNamesArray[x]
        a = _filerParams(paramsNamesArray[x])
        paramsTuple[paramsNamesArray[x]] = a

    return paramsTuple


# b = get_all_params_erpe()