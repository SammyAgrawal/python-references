import pandas


book = pandas.read_excel("pandatest.xlsx")

rich= (book[book.Salary>=200000])

rich = rich.fillna({
        'Status':'rich'})
#print (rich)
writer= pandas.ExcelWriter("pandatest.xlsx", engine='xlsxwriter')
rich.to_excel(writer, sheet_name="Sheet1", startrow=5)
writer.save()