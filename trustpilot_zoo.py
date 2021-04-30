from bs4 import BeautifulSoup
import requests

ws = requests.get('https://www.trustpilot.com/categories/animal_parks_zoo').text
soup = BeautifulSoup(ws, 'lxml')
zoo_lst = soup.find('div', class_='styles_businessUnitCardsContainer__1ggaO')
name = zoo_lst.find('div', class_='styles_businessTitle__1IANo').text
review = zoo_lst.find('div', class_='styles_textRating__19_fv').text
typ = zoo_lst.find('div', class_='styles_categories__c4nU-').text

c = 0
print('\nBEST IN ANIMAL PARKS & ZOO\n')
print('*' * 90)
print('NAME --> ', name)
print('REVIEW --> ', review)
print('TYPE --> ', typ)

# To get park/zoo link
possible_links = zoo_lst.find_all('a', class_='link_internal__YpiJI link_wrapper__LEdx5')
for link in possible_links:
    if c == 1:
        break
    if link.has_attr('href'):
        print('WEBSITE LINK --> ', 'https://www.trustpilot.com' + link.attrs['href'])
        c = +1
print('*' * 90)
