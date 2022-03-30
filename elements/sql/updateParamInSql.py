def updateParamsInSQL(connection,
                      cursor,
                      tableName,
                      columnName,
                      paramsArray=None,
                      findParam=None,
                      columnName1=None,
                      findParam2=None,
                      columnName2=None):

    # Input data:
    # 1. connection to sql
    # 2. cursor from sql connection
    # 3. table name in arhive
    # 4. column name from sql Table
    if findParam is None and findParam2 is None:
        # remove old position from arhive
        query = f"""TRUNCATE TABLE `{tableName}`"""
        cursor.execute(query)
        connection.commit()

        # Update params in SQL base
        for x in range(len(paramsArray)):
            query = f"""INSERT INTO `{tableName}` (`{columnName}`) VALUES ("{str(paramsArray[x])}")"""
            cursor.execute(query)
            connection.commit()

    elif findParam is not None and findParam2 is None:
        # remove from sql old parameters
        for x in range(len(paramsArray)):
            query = f"""DELETE FROM `{tableName}` WHERE `{columnName}` = '{findParam}'"""
            cursor.execute(query)
            connection.commit()

        for x in range(len(paramsArray)):
            query = f"""INSERT INTO `{tableName}` (`{columnName}`, `{columnName1}`) VALUES ("{str(findParam)}","{str(paramsArray[x])}")"""
            cursor.execute(query)
            connection.commit()


