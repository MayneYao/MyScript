import win32com.client as win32
import requests
from bs4 import BeautifulSoup as bs
from time import sleep

x1 = win32.gencache.EnsureDispatch("Excel.Application")
ss = x1.Workbooks.Add()
sh = ss.ActiveSheet
x1.Visible = True
#盗版的office打开有个确认按钮要点一下，不然不会开始下一步操作
sleep(3)

r = requests.get("http://kafka.apache.org/documentation")
soup = bs(r.text,"html5lib")
x = soup.find_all("table")
#手动确认开始的6张表格
# for i in range(7):·
#    print(x[i])
x = x[0:7]

#把每个td的内容写到对应的excel格子中
cell_y=1
for tb in x:
    for tr in tb.find_all("tr"):
        v = [td.text for td in tr.find_all("td")]
        for i in range(len(v)):
            sh.Cells(cell_y,i+1).Value = v[i] 
        cell_y +=1
