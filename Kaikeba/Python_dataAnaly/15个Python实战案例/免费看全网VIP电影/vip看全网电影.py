#-*- coding:UTF-8 -*-
url = 'https://okjx.cc/?url='
import sys

import webbrowser

sys.path.append("libs")

##修改链接
urls = 'https://v.qq.com/x/cover/r2eatcdcv2deik5.html'
print(url+urls)

webbrowser.open(url+urls)

print(webbrowser.get())