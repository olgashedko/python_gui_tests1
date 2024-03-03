from comtypes.client import CreateObject
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

x1 = CreateObject("Excel.Application", dynamic=True)
x1.Visible = True
wb = x1.Workbooks.Add()
for i in range(10):
    x1.Range["A%s" % (i+1)].Value[()] = "group %s" % i
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
x1.Quit()