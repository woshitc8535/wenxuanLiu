import requests
from bs4 import BeautifulSoup
from urllib.request import quote

while True:
    film_name = input('请输入电影名字(退出输入q)：')
    if film_name == 'q':
        break
    name_code = quote(film_name.encode('gbk'))
    url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword=' + name_code

    res = requests.get(url)
    res.encoding = 'gbk'
    bs = BeautifulSoup(res.text, 'html.parser')
    num = bs.find('td', attrs={'bgcolor': "#FFFFFF"})

    count = num.text.strip().split('/')[1][:-3]
    if count == '0':
        print('电影《{}》没有找到资源'.format(film_name))
    else:
        print('电影《{}》找到{}个资源'.format(film_name, count))

        href_list = bs.find_all('table')[1:]
        for h in href_list:
            link = 'https://www.ygdy8.com' + h.a['href']
            res2 = requests.get(link)
            res2.encoding = 'gbk'
            bs2 = BeautifulSoup(res2.text, 'html.parser')
            link2 = bs2.find_all('table')
            print(link2[1].a['href'])

