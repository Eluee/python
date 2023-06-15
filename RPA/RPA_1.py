from openpyxl import Workbook
from random import *

wb = Workbook()
ws = wb.active

# 현제 활성화 되어있는 시트에 행을 추가.
ws.append(["번호", "영어", "수학"])
for i in range(1, 11):
    ws.append([i, randint(0, 100), randint(0, 100)])

wb.save("testsampleb.xlsx")
wb.close()