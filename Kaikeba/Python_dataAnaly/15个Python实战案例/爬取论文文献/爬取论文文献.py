import requests
from bs4 import BeautifulSoup
import xlsxwriter

excelName = input('请输入excel名：')
titelName = input('请输入需要爬取的标题：')
workbook = xlsxwriter.Workbook(excelName+'.xlsx')
# 创建一个sheet
worksheet = workbook.add_worksheet()
href = []
text = []
for s in range(2,20):
    url = 'https://s.ixueshu.com/index.html?q='+titelName+'&page='+str(s)
    user_agent = {
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.find_all('a',target='_blank')
    for i in range(1,len(items)-10,2):
        print(str(items[i].get("href"))+str(items[i].get_text()))
        href.append(items[i].get("href"))
        text.append(items[i].get_text())

worksheet.write(0, 0, "下载链接")
worksheet.write(0, 1, "论文标题标题")
for j in range(0,len(href)):
    worksheet.write(j+1, 0, href[j])
    worksheet.write(j+1, 1, text[j])
workbook.close()