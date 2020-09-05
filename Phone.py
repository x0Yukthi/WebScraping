'''This is used to find different prices of a phone '''
import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
wpage = requests.get(url)
BS = BeautifulSoup(wpage.content, 'html.parser')
res = BS.find(id='container')
mob_ele = res.find('div', class_='t-0M7P')

for m_ele in mob_ele:
    product = m_ele.find('div', class_='_3wU53n')
    price = m_ele.find('div', class_='_2o7WAb')
    rating = m_ele.find('div', class_='niH0FQ')
    if None in (product, price, rating):
        continue
    print(product.text)
    print(price.text)
    print(rating.text)
    print()
