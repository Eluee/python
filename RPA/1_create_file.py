from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "mySheet"

ws.append(["번호", "영어", "수학"]) 

wb.save("sample.xlsx")
wb.close()
