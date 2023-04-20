from openpyxl_practice import Workbook
wb = Workbook()
ws = wb.active
ws.title = "mySheet"
wb.save("sample.xlsx")
wb.close()
