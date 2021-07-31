import requests
# import lxml
from bs4 import BeautifulSoup
import os
if not os.path.exists("福妻高照"):
    os.makedirs("福妻高照")
url="https://book.qidian.com/info/1016755751#Catalog"
req=requests.get(url=url)
req.encoding="utf-8"
print("响应码",req.status_code)
html=req.text
bf=BeautifulSoup(html,"lxml")
# print(bf)
ul=bf.find_all("ul",class_="cf")
# print(ul)
bf1=BeautifulSoup(str(ul[0]),"lxml")
# print(bf1)
a_list=bf1.find_all("a")
# print(a_list)
def getDanzData(name,url):
    name=name+".txt"
    url="https:"+url
    req=requests.get(url=url)
    req.encoding="utf-8"
    html=req.text
    bf=BeautifulSoup(html,"lxml")
    # print(bf)
    div = bf.find_all("div", class_="read-content j_readContent")
    # print(div)
    txt=div[0].text
    with open("福妻高照/%s"%name,"w",encoding="utf-8")as file:
        file.write(txt)
        file.close()
    print("%s下载成功"%name)
for item in a_list:
    name=item.string
    url=item.get("href")
    getDanzData(name,url)