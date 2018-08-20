import xlrd
import json

data = xlrd.open_workbook('Winedataset.xlsx')
table = data.sheets()[0]

a = []
for i in range(1,table.nrows):
    a.append(table.row_values(i)[2:])

with open('dataset.json', 'w') as f:
    f.write('dataset = ' + json.dumps(a))
