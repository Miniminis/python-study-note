"""
절차지향형 vs 객체지향 프로그래밍
"""

# 절차지향형 프로그래밍 

from openpyxl import *
wb = load_workbook('exam.xlsx')
print(wb.sheetnames)

ws = wb.active
print(ws)

g = ws.rows  # 모든 행을 가져와 객체로 반환
cells = next(g)
print(cells)

keys = []
for cell in cells:
    keys.append(cell.value)    # cell 의 value 에 접근하여 가져옴 

print(keys)


student_data = []
for row in g:
    dic = {k: c.value for k, c in zip(keys, row)}
    student_data.append(dic)

print(student_data)



