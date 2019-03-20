from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url ="https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf-8')
soup = BeautifulSoup(html_content, "html.parser")
section = soup.find("section","section chart-grid")
li_list = section.div.ul.find_all("li")
dic_list = []

options = {
    'default_search': 'ytsearch',
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
}

for li in li_list:
    h4 = li.h4.a
    h3 = li.h3.a
    namesong = h3.string
    artis = h4.string

    dic = OrderedDict({
        "Names" : namesong,
        "Artis" : artis,
    })
    dic_list.append(dic)

    dl = YoutubeDL(options)
    dl.download([namesong])

pyexcel.save_as(records=dic_list, dest_file_name="itunes.xlsx")