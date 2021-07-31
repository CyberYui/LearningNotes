import pandas as pd
import os
A_DIR = os.path.dirname(os.path.abspath(__file__))
path = A_DIR+'/未处理/'
paths = A_DIR+'/已处理/'
file = []
filename_list = os.listdir(path)
for i in filename_list:
    file.append(path+i)
li = []
for i in file:
    li.append(pd.read_excel(i))
writer = pd.ExcelWriter(paths+'合并后文件.xlsx')
pd.concat(li).to_excel(writer, 'Sheet1', index=False)
writer.save()
