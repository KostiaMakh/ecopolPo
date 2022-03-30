from elements.sql.connectSql import connectToSql
from widgets.objInf_w.objInfoWindow import mainObj

def add_equip_params_in_sql(type, mainObj):
    if type == 'erpe':
        query = f"""INSERT INTO `erpe_arhive` (
                        `id`,
                        `gap`,
                        `cw`,
                        `ch`,
                        `hUnload`,
                        `cp`,
                        `protokol`) VALUES (
                            {int(mainObj.erpe.proposal_ID)},
                            {int(mainObj.erpe.gap)},
                            {int(mainObj.erpe.channelWidth)},
                            {int(mainObj.erpe.channelDepth)},
                            {int(mainObj.erpe.unloadH)},
                            '{str(mainObj.erpe.controlPanel)}',
                            '{str(mainObj.erpe.connection)}')
                       """
        _addNewPosition_toArhive(query)

    elif type == 'rvgo':
        query = f"""INSERT INTO `rvgo_arhive` (
                        `id`,
                        `gap`,
                        `cw`,
                        `screen_height`,
                        `ch`,
                        `hUnload`,
                        `cp`,
                        `protokol`) VALUES (
                            {int(mainObj.rvgo.proposal_ID)},
                            {int(mainObj.rvgo.gap)},
                            {int(mainObj.rvgo.channelWidth)},
                            {int(mainObj.rvgo.screenHeight)},
                            {int(mainObj.rvgo.channelDepth)},
                            {int(mainObj.rvgo.unloadH)},
                            '{str(mainObj.rvgo.controlPanel)}',
                            '{str(mainObj.rvgo.connection)}')
                       """
        _addNewPosition_toArhive(query)

def addNewPosition_RTO_ToArhive(mainObj):
    con = connectToSql()
    connection = con[0]
    cursor = con[1]

    query = f"""INSERT INTO `rto_arhive` (
                `id`,
                `gap`,
                `cw`,
                `ch`,
                `hUnload`,
                `cp`,
                `protokol`) VALUES (
                    {int(mainObj.rto.proposal_ID)},
                    {int(mainObj.rto.gap)},
                    {int(mainObj.rto.channelWidth)},
                    {int(mainObj.rto.channelDepth)},
                    {int(mainObj.rto.unloadH)},
                    '{str(mainObj.rto.controlPanel)}',
                    '{str(mainObj.rto.connection)}')
               """
    cursor.execute(query)
    connection.commit()

def _addNewPosition_toArhive(query):
    con = connectToSql()
    connection = con[0]
    cursor = con[1]
    cursor.execute(query)
    connection.commit()
