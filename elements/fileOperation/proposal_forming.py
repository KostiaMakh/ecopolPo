def create_proposal(calculationFile, proposalSample, proposalSavingDirectory, fileName):
    import win32com.client as win32
    import xlwings
    import time

    # control input params. Is data float or int.
    def float_control(num):
        try:
            float(num)
            for x in range(1, str(num).__len__()):
                if str(num)[x] == '.':
                    if int(str(num)[(x + 1):]) != 0:
                        return True
                    else:
                        return False
                else:
                    pass
            return False
        except:
            return False


    arr = []
    for x in range(1, 120):
    
        variable = calculationFile.sheets['tkp_params'].range(f'B{x}').value
        value_of_bookmark = calculationFile.sheets['tkp_params'].range(f'C{x}').value
    
        if variable is not None or value_of_bookmark is not None:
            arr.append([variable, value_of_bookmark])

    word = win32.gencache.EnsureDispatch('Word.Application')

    word.Documents.Open(str(proposalSample))
    word.Visible = True

    for x in range(arr.__len__()):
        # Choose company favicon in proposal
        if arr[x][0] == 'prop_comp':
            if arr[x][1] == 'ТПП Экополимер':
                word.ActiveDocument.Bookmarks('eco_ukr').Range.Text = ''
                word.ActiveDocument.Bookmarks('My_pr').Range.Text = ''
            elif arr[x][1] == 'НПФ Экополимер':
                word.ActiveDocument.Bookmarks('tpp').Range.Text = ''
                word.ActiveDocument.Bookmarks('My_pr').Range.Text = ''
            else:
                word.ActiveDocument.Bookmarks('tpp').Range.Text = ''
                word.ActiveDocument.Bookmarks('eco_ukr').Range.Text = ''

        if word.ActiveDocument.Bookmarks.Exists(f'{arr[x][0]}') == True:
            if arr[x][1] == -1:
                pass
            elif arr[x][1] == -2:
                word.ActiveDocument.Bookmarks(f'{str(arr[x][0])}').Range.Text = ''
            else:
                # try:
                #     try:
                #         word.ActiveDocument.Bookmarks(f'{str(arr[x][0])}').Range.Text = int(arr[x][1])
                #     except:
                #         word.ActiveDocument.Bookmarks(f'{str(arr[x][0])}').Range.Text = str(arr[x][1])
                # except:
                #     pass
                try:
                    try:
                        if float_control(arr[x][1]) is True:
                            word.ActiveDocument.Bookmarks(f'{str(arr[x][0])}').Range.Text = float(arr[x][1])
                        else:
                            word.ActiveDocument.Bookmarks(f'{str(arr[x][0])}').Range.Text = int(arr[x][1])
                    except:
                        word.ActiveDocument.Bookmarks(f'{str(arr[x][0])}').Range.Text = str(arr[x][1])
                except:
                    pass
    try:
        word.ActiveDocument.Bookmarks('Validity').Range.Text = str(time.strftime('%d.%m.%y', time.localtime(time.time()+30*24*60*60)))
    except:
        pass

    word.ActiveDocument.SaveAs2(str(proposalSavingDirectory + '\\' + fileName + '.docx'))
    word.Quit()

    # xl = win32.gencache.EnsureDispatch('Excel.Application')
    # ss = xl.Workbooks.Add()
    # sh = ss.ActiveSheet
    #
    # sh.Cells(2, 2).Value = 'Hello! ITS ME'
    #
    # xl.Visible = True
    # time.sleep(1)
    #
    # sh.Cells(1, 1).Value = 'Hacking Excel with Python Demo'
    #
    # time.sleep(1)
    # for i in range(2, 10):
    #     sh.Cells(i, 1).Value = 'Line %i' % i
    #     time.sleep(1)
    
    # ss.Close(False)
    # xl.Application.Quit()
