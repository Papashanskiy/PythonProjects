import xlsxwriter
import sqlite3
import pprint

conn = sqlite3.connect('my_db.db')
c = conn.cursor()
a = c.execute('SELECT * FROM users').fetchall()


workbook = xlsxwriter.Workbook('DB_table.xlsx')
worksheet = workbook.add_worksheet()
row = 1
col = 0

cell_format = workbook.add_format()

worksheet.write(0, 0, 'Username')
worksheet.write(0, 1, 'Email')
worksheet.write(0, 2, 'Age')
worksheet.write(0, 3, 'Favorite color')
for username, email, age, fav_color in a:
    worksheet.write(row, col, username)
    worksheet.write(row, col+1, email)
    worksheet.write(row, col+2, age)
    worksheet.write(row, col+3, fav_color)
    row += 1


worksheet.write(row+1, 0, 'Total users:')
worksheet.write(row+1, 1, len(a))

workbook.close()
