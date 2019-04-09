import requests
from bs4 import BeautifulSoup

# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#
# novel = res.text
#
# k = open('《三国演义》.txt', 'a+',encoding='utf-8')
#
# k.write(novel)
#
# k.close()

# res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
# article=res.text
# k = open('《HTTP状态响应码》.txt','a+',encoding='utf-8')
# k.write(article)
# k.close
#
#
# res_foods = requests.get('http://www.xiachufang.com/explore/')
# # 获取数据
# bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# # 解析数据
# dish_list=[]
# list_foods = bs_foods.find_all('div',class_='info pure-u')
# # 查找最小父级标签
# for i in range(len(list_foods)):
#     list1=[]
#     tag_a = list_foods[i].find('a')
#
#     # 提取第0个父级标签中的<a>标签
#     #print(tag_a.text[17:-13])
#     # 输出菜名，使用[17:-13]切掉了多余的信息
#     URL=('http://www.xiachufang.com'+tag_a['href'])
#     # 输出URL
#     tag_p=list_foods[i].find('p',class_='ing ellipsis')
#     #print(tag_p.text)
#     #提取食材
#     list1=[tag_a.text[17:-13],URL,tag_p.text]
#     dish_list.append(list1)
# print(dish_list)

# res = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png' )
# k=open('图片.jpg','wb')
# k.write(res.content)
# k.close()

res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
k=open('音乐.mp3','wb')
k.write(res.content)
k.close()