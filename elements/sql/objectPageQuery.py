from elements.sql.connectSql import connectToSql

objTableInSql = 'params_object'
objSql_column0 = 'param_name'
objSql_column1 = 'val0'

con = connectToSql()
connection = con[0]
cursor = con[1]

def get_all_params():


    query = f"""SELECT * FROM `{objTableInSql}`"""

    cursor.execute(query)
    params_arh = cursor.fetchall()

    para_names_in_sql = {0: 'Менеджер',
                         1: 'Страна'}

    def _filterParams(paramsID):
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

    manager = _filterParams(0)
    county = _filterParams(1)\

    return [manager, county]

def update_obj_params(newParmsTable):

    query = f"""TRUNCATE TABLE `{objTableInSql}`"""
    connection.ping()
    cursor.execute(query)
    connection.commit()

    query = f"""INSERT INTO `{objTableInSql}` (`{objSql_column0}`, `{objSql_column1}`) VALUES """
    for x in range(0, len(newParmsTable)):
        qr = f"""('{newParmsTable[x][0]}', '{newParmsTable[x][1]}'), """
        query = query + qr
    query = query[:-2]

    connection.ping()
    cursor.execute(query)
    connection.commit()
#
# b = get_all_params()