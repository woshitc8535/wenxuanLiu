import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.forc.work')
soup = BeautifulSoup(res.text, 'html.parser')
article_list=[]
area = soup.find('div', class_='content-area')
article = area.find_all('header', class_='entry-header')
for i in range((len(article))):
    url = article[i].find('a')['href']
    name = article[i].find('h2').text
    time = article[i].find('time').text
    article_list.append([url,name,time])
print(article_list)


