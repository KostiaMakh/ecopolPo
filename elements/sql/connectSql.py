import pymysql


def connectToSql():
        host = 'cancer91.beget.tech'
        user = 'cancer91_calc'
        password = 'FDS147mn2659'
        db_name = 'cancer91_calc'

        connection = None
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        cursor = connection.cursor()

        return [connection, cursor]

if __name__=="__main__":
    pass