def addPositionToCMB(array, cmbBox):
    for a in range(len(array)):
        if isinstance(array[a], list):
            cmbBox.addItem(str(array[a][0]))
        else:
            cmbBox.addItem(str(array[a]))

