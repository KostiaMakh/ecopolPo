import win32com.client as win32
import xlwings
import time

wb = xlwings.Book("D:\\1_newProgram(ver.2)\\docs\\initial\\РЕШЕТКА.xlsx")
arr = []
for x in range(1, 120):

    variable = wb.sheets['tkp_params'].range(f'B{x}').value
    value_of_bookmark = wb.sheets['tkp_params'].range(f'C{x}').value

    if variable is not None or value_of_bookmark is not None:
        arr.append([variable, value_of_bookmark])


word = win32.gencache.EnsureDispatch('Word.Application')

word.Documents.Open("D:\\1_newProgram(ver.2)\\docs\\ТЕХНИКО.docx")
word.Visible = True

for x in range(arr.__len__()):

    if word.ActiveDocument.Bookmarks.Exists(f'{arr[x][0]}') == True:
        if arr[x][1] == -1:
            pass
        elif arr[x][1] == -2:
            word.ActiveDocument.Bookmarks(f'{str(arr[x][0])}').Range.Text = ''
        else:
            try:
                try:
                    word.ActiveDocument.Bookmarks(f'{str(arr[x][0])}').Range.Text = int(arr[x][1])
                    print(f'{arr[x][0]} = {arr[x][1]}')
                except:
                    word.ActiveDocument.Bookmarks(f'{str(arr[x][0])}').Range.Text = str(arr[x][1])
                    print(f'{arr[x][0]} = {arr[x][1]}')
            except:
                pass
    else:
        print(12)
word.ActiveDocument.Bookmarks('Validity').Range.Text = str(time.strftime('%d.%m.%y', time.localtime(time.time()+30*24*60*60)))

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
