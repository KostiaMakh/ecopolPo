from elements.sql.connectSql import connectToSql

arhTableInSql = 'arhive'
arhTableInSql0 = 'param_name'
arhTableInSql1 = 'val_1'
arhTableInSql2 = 'min'
arhTableInSql3 = 'max'
arhTableInSql4 = 'sheet'
arhTableInSql5 = 'cell'
arhTableInSql6 = 'link'


def get_arh_proposal():
    con = connectToSql()
    connection = con[0]
    cursor = con[1]

    query = f"""SELECT `id`, `city`, `object`, `location`, `position`, `mark`, `date_ex`, `eqip_code`, `manualChange` FROM `{arhTableInSql}` WHERE `id` > 8500"""

    cursor.execute(query)
    params_arh = cursor.fetchall()

    return params_arh

def get_eqiup_params(equip_type, main_obj):
    con = connectToSql()
    connection = con[0]
    cursor = con[1]

    if equip_type == 'rto':
        query = f'''SELECT rto_arhive.`gap`, rto_arhive.`cw`, rto_arhive.`ch`, rto_arhive.`hUnload`, rto_arhive.`cp`, 
        rto_arhive.`protokol`, arhive.`ip`, arhive.`material`, arhive.`menedger`, arhive.`country`, arhive.`tkp_company`
FROM rto_arhive INNER JOIN arhive ON (rto_arhive.id=arhive.id) WHERE rto_arhive.id = {int(main_obj.rto.proposal_ID)}'''

        cursor.execute(query)
        params_arh = cursor.fetchall()

        main_obj.rto.gap = params_arh[0][0]
        main_obj.rto.channelWidth = params_arh[0][1]
        main_obj.rto.channelDepth = params_arh[0][2]
        main_obj.rto.unloadH = params_arh[0][3]
        main_obj.rto.controlPanel = params_arh[0][4]
        main_obj.rto.connection = params_arh[0][5]
        main_obj.rto.driveIP = str(params_arh[0][6]).replace('IP ', '')
        main_obj.rto.material = params_arh[0][7]
        main_obj.manager = params_arh[0][8]
        main_obj.country = params_arh[0][9]
        main_obj.company = params_arh[0][10]

        return params_arh



# b = get_all_params()