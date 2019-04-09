import requests
from bs4 import BeautifulSoup

from urllib.request import quote

# quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
# file_name = input('pls print what film you like!\n')
url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='
path = url + quote('复仇者联盟', encoding='gbk')

res = requests.get(path)

soup = BeautifulSoup(res.content.decode('gbk', 'ignore'), 'html.parser')
filelist = []
page = (soup.find('div', class_='co_content8'))
try:
    content = page.find_all('table')
    for i in range((len(page.find_all('table')))):
        tail = content[i].find('a')['href']
        name = content[i].find('a').text
        print('www.ygdy8.com' + tail, name)
        newurl = 'www.ygdy8.com' + tail
        newres = requests.get(newurl)
        newsoup = BeautifulSoup(newres.content.decode('gbk', 'ignore'), 'html.parser')
        link = newsoup.find('table',style=)




except AttributeError:
    print('there is no result from your search')
# f=open('想看的电影.txt','a+',encoding='utf-8')
# for x in filelist:
#     for m in x:
#         f.write(m)
#         f.write('\n')
# f.close()
