
from openpyxl import load_workbook

wb_val = load_workbook(filename='Results.xlsx', data_only=True)

sheet_val = wb_val['Sheet1']

D4_val = sheet_val['D4'].value

print(D4_val)
