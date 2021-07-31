#爬取阳光电影的最新电影#

from pyquery import PyQuery as pq
import requests
def pagep(page):
    page_url='http://www.ygdy8.com/html/gndy/dyzz/list_23_%s.html'%page
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    sponse=requests.get(url=page_url,headers=headers)
    sponse.encoding='gbk'
    decoding_ =sponse.text
    doc=pq(decoding_)
    The_body_of_the=doc('.ulink').items()
    for i in The_body_of_the:

        #To_find_the=i.find('td b a').text()
        #To_find_the=i.text()
        #A_newline=To_find_the.replace(' ','\n')
        URL = 'http://www.ygdy8.com'

        The_movie_name=i.text()
        The_film_addresses=URL+i.attr('href')


        #因为下载的地址全是ftp开头 mkv结尾的 所以决定趴下来
        #Because the download address is all FTP beginning MKV end so decided to sit down
        The_second_request=requests.get(url=The_film_addresses,headers=headers)
        The_second_request.encoding='gbk'
        The_decoding =The_second_request.text
        #解析我们想要的下载地址
        The_doc=pq(The_decoding)
        Download_address=The_doc('.co_content8').items()
        for The_i in Download_address:
            download_address=The_i.find('td a').text()

            Storage={
                '电影名字':The_movie_name,
                '电影的地址':The_film_addresses,
                '电影下载地址':download_address
            }
            print(Storage)

#循环次数可以改的 1代表一页 一页中有10多条电影信息
for cycle in range(167):
    pagep(cycle)