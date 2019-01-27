import xlsxwriter

workbook = xlsxwriter.Workbook('table_4.xlsx')
worksheet = workbook.add_worksheet()

expenses = (
    ['Car', 20000],
    ['House', 40000],
    ['Wife', 0],
    ['Cat', 100]
)
expenses_2 = [
    ['Car', 20000],
    ['House', 40000],
    ['Wife', 0],
    ['Cat', 100]
]

row = 0
col = 0

for item, cost in expenses_2:
    worksheet.write(row, col, item)
    worksheet.write(row, col+1, cost)
    row += 1

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()
