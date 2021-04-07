import faker
import xlwt

data=faker.Faker()
wk=xlwt.Workbook()
ws=wk.add_sheet("Sheet1")

for i in range (0,1000):
    ws.write(i,0, data.name())
    ws.write(i,1, data.email())
    ws.write(i, 2, data.address())

    wk.save("C:\Test\Results.xls")


