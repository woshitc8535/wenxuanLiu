import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start=0&filter='
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
page = soup.find('div', class_='paginator').find_all('a')
list1=[]
for i in range(len(page) - 1):
    tail = page[i]['href']
    new_url = 'https://movie.douban.com/top250' + tail
    Nres = requests.get(new_url)
    Nsoup = BeautifulSoup(Nres.text, 'html.parser')
    article = Nsoup.find('div', class_='article')
    items_number = article.find_all('li')

    for x in range((len(items_number))):
        link = items_number[x].find('a')['href']
        name = items_number[x].find('span', class_='title').text
        number = items_number[x].find('em').text
        comment = items_number[x].find('span', class_='inq')

        grade = items_number[x].find('span', class_='rating_num').text

        list1.append([number,name,grade,comment,link])

print(list1)



