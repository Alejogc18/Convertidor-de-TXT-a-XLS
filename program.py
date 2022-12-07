import xlwt
import xlrd
f = open('"nombre de su archivo txt".txt', 'r+')
row_list = []
for row in f:
    row_list.append(row.split())
column_list = zip(*row_list)
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Sheet1')
i = 0 
for column in column_list:
    for item in range(len(column)):
        worksheet.write(item, i, column[item])
    workbook.save('"titulo que tendra el excel".xls')
    i+=1