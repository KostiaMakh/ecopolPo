from PyQt5 import QtWidgets

def add_items_into_table(table_name, values_array, vertical_headers_number = False):
    if vertical_headers_number == False:
        for x in range(0, len(values_array)):
            for y in range(0, len(values_array[x])):
                table_name.setItem(x, y, QtWidgets.QTableWidgetItem(str(values_array[x][y])))
    else:
        vals = make_headers_array(values_array)
        table_name.setVerticalHeaderLabels(vals[0])
        add_items_into_table(table_name, vals[1], vertical_headers_number=False)

def make_headers_array(input_arr):
    header_arr = []
    for x in range(len(input_arr)):
        header_arr.append(input_arr[x][0])

    values_arr=[]
    for x in range(len(input_arr)):
        bufer = []
        for y in range(1, len(input_arr[x])):
            bufer.append(input_arr[x][y])
        values_arr.append(bufer)

    return [header_arr, values_arr]