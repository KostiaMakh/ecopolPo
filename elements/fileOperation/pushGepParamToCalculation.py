from elements.sql.connectSql import connectToSql
import xlwings

# Push general params from sql to page 'Параметры'

def pushParamsToFile(xlWorkBook):
    connect = connectToSql()
    sqlTableName = "generalParam"
    sqlColumnName1 = "param_name"
    sqlColumnName2 = "param_value"
    sqlColumnName3 = "page"
    sqlColumnName4 = "cell"

    query = f"""SELECT DISTINCT `{sqlColumnName1}`,
                                `{sqlColumnName2}`,
                                `{sqlColumnName3}`,
                                `{sqlColumnName4}` FROM `{sqlTableName}`"""

    connect[1].execute(query)
    params = connect[1].fetchall()

    print(params)
    for x in range(len(params)):
        xlWorkBook.sheets[f'{params[x][2]}'].range(f'{params[x][3]}').value = params[x][1]

