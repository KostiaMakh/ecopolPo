def getUniqFromColumn(connection,
                      cursor,
                      tableName,
                      columnName,
                      findParam=None,
                      findParamCategory=None,
                      findParam2=None,
                      findParamCategory2=None) -> object:

    # Input data:
    # 1. connection to sql
    # 2. cursor from sql connection
    # 3. table name in arhive
    # 4. column name from sql Table

    # Get query from SQL
    if findParam is None and findParam2 is None:
        query = f"""SELECT DISTINCT `{columnName}` FROM `{tableName}`"""
    elif findParam2 is None:
        query = f"""SELECT DISTINCT `{columnName}` FROM `{tableName}` WHERE `{findParamCategory}`='{findParam}'"""
    else:
        query = f"""SELECT DISTINCT `{columnName}` FROM `{tableName}` WHERE `{findParamCategory}`='{findParam}' AND `{findParamCategory2}`='{findParam2}'"""
        print(query)


    cursor.execute(query)

    ret = cursor.fetchall()

    # Create new array and sort fetch low-to-high
    objects = []


    for a in range(len(ret)):
        # Special method for int date
        if findParam == 'Прозор, мм'\
                or findParam == 'Ширина канала, мм'\
                or findParam == 'Высота выгрузки, мм'\
                or findParam == 'Привод':
            try:
                objects.append(int(ret[a][0]))
            except: pass
        else:
            objects.append(ret[a][0])

    objects.sort()

    # def return array of sorted string parameters.
    return objects


def getChanelDepth(connection,
                   cursor,
                   tableName,
                   minChanelDepth,
                   maxChanelDepth,
                   findParam,
                   findParamCategory,
                   findParam2,
                   findParamCategory2
                   ) -> object:

    # get minimal channel
    query = f"""SELECT DISTINCT `{minChanelDepth}` FROM `{tableName}` WHERE `{findParamCategory}`='{findParam}' AND `{findParamCategory2}`='{findParam2}'"""
    print(query)
    cursor.execute(query)
    ret = cursor.fetchall()
    min_ch = ret[0][0]

    # get maximal channel
    query = f"""SELECT DISTINCT `{maxChanelDepth}` FROM `{tableName}` WHERE `{findParamCategory}`='{findParam}' AND `{findParamCategory2}`='{findParam2}'"""
    print(query)
    cursor.execute(query)
    ret = cursor.fetchall()
    max_ch = ret[0][0]

    objects = []
    a = int(min_ch)-100
    while a < int(max_ch):
        a = a + 100
        objects.append(a)

    objects.sort()
    return objects
