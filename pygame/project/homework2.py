import requests
from bs4 import BeautifulSoup

res = requests.get('http://books.toscrape.com/')
bs_res = BeautifulSoup(res.text, 'html.parser')
library = bs_res.find('div', class_='side_categories')
categories = library.find_all('a')
list1 = []
for i in range((len(categories))):
    name = categories[i].text.strip()
    list1.append(name)
print(list1)

# 所有图书
Allbook_list = []
book = bs_res.find_all('article', class_='product_pod')
for i in range((len(book))):
    rate = book[i].find('p')['class'][1]
    price= book[i].find('p',class_='price_color')
    book_name= book[i].find_all('a')[1]['title']
    Allbook_list.append([book_name,rate,price.text])
print(Allbook_list)



