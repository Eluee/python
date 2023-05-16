from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(["번호", "영어", "수학"])

