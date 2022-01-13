import xlrd

file_location = (r"C:\Users\Rishabh\PycharmProjects\Py-for-Infosec\Problems\Book2.xlsx")
#giving file location

workbook_test = xlrd.open_workbook(file_location)#opening file

sheet_test = workbook_test.sheet_by_index(0)

sheet_test.cell_value(0,0)

