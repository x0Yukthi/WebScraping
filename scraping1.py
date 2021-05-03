from bs4 import BeautifulSoup
import requests

url = requests.get(
    "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DAPPLE").text
soup = BeautifulSoup(url, 'lxml')
# To get the text from web page
res = soup.find('div', class_='_1YokD2 _2GoDe3')
phn = res.find('div', class_='_3pLy-c row')
phn_name = phn.find('div', class_='_4rR01T').text
phn_cong = phn.find('div', class_='fMghEO').text
phn_price = phn.find('div', class_='_30jeq3 _1_WHN1').text
actual_price = phn.find('div', class_='_3I9_wc _27UcVY').text
emi = phn.find('div', class_='_2ZdXDB').text

# To print the details
print(f'''

PHONE DETAILS

PHONE NAME --> {phn_name}
CONFIGURATION --> {phn_cong}
PRODUCT PRICE --> {actual_price}
OFFER PRICE --> {phn_price}
OTHER DETAILS --> {emi}'

''')

