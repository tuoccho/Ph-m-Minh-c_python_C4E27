from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url ="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode('utf-8')
soup = BeautifulSoup(html_content, "html.parser")

# with open("Cafef.html","wb") as f:
#     f.write(raw_data)

table = soup.find("table", id = "tableContent")
list_tr = table.tr.find_all('tr')
dic_list = []


for i in list_tr:
    list_td = i.find_all('td')
    # print(td)
    dic = OrderedDict({})
    for a in range(len(list_td)):
        
        so = list_td[a].string

        if a == 0:
            dic['STT'] = so
        elif a == 1:
            dic['Quý 4-2016'] = so
        elif a == 2:
            dic['Quý 1-2017'] = so
        elif a == 3:
            dic['Quý 2-2017'] = so
        elif a == 4:
            dic['Quý 3-2017'] = so
    dic_list.append(dic)
print(dic_list)
# pyexcel.save_as(records = dic_list, dest_file_name = "cafef.xlsx")
