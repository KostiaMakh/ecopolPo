from elements.sql.connectSql import connectToSql
import time


def addNewPositionToArhive(city='-',
                           object='-',
                           location='-',
                           position='-',
                           mark='-',
                           manager='-',
                           equip_price=0,
                           cp_price=0,
                           weight=0,
                           ip='-',
                           power=0,
                           material='-',
                           executor='-',
                           equip_code='-',
                           description='-',
                           country='',
                           tkp_company=''):
    con = connectToSql()
    connection = con[0]
    cursor = con[1]

    timeNOW = time.strftime("%d.%m.%Y %H:%M:%S")

    query = f"""INSERT INTO `arhive` (
                `city`,
                `object`,
                `location`,
                `position`,
                `mark`,
                `menedger`,
                `eqip_price`,
                `cp_price`,
                `weight`,
                `ip`,
                `power`,
                `material`,
                `date_ex`,
                `executer`,
                `eqip_code`,
                `description`,
                `country`,
                `tkp_company`) VALUES (
                    '{str(city)}',
                    '{str(object)}',
                    '{str(location)}',
                    '{str(position)}',
                    '{str(mark)}',
                    '{str(manager)}',
                    {int(equip_price)},
                    {int(cp_price)},
                    {int(weight)},
                    '{str(ip)}',
                    {float(power)},
                    '{str(material)}',
                    '{str(timeNOW)}',
                    '{str(executor)}',
                    '{str(equip_code)}',
                    '{str(description)}',
                    '{(str(country))}',
                    '{str(tkp_company)}')
               """
    cursor.execute(query)
    connection.commit()

    query = f"""SELECT `id` FROM `arhive` WHERE
                    `city` = '{str(city)}' AND
                    `object` = '{str(object)}' AND 
                    `mark` = '{str(mark)}' AND
                    `date_ex` = '{str(timeNOW)}'
                   """

    cursor.execute(query)
    result = cursor.fetchall()
    print(result[0])

    return result[0][0]

def addProposalNameToArhive(id, proposal_name):
    con = connectToSql()
    connection = con[0]
    cursor = con[1]

    query = f"""UPDATE `arhive` SET `proposal_name`='{str(proposal_name)}' WHERE `id`={id}"""
    cursor.execute(query)
    connection.commit()
