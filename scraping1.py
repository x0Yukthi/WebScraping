from bs4 import BeautifulSoup
import requests
import time
def find_phone():
    url = requests.get("https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DAPPLE").text
    soup = BeautifulSoup(url,'lxml')
    # To get the text from web page
    result = soup.find_all('div', class_ ='_2kHMtA')
    print('\nPHONE DETAILS\n')
    for res in result:
        phn_name= res.find('div',class_='_4rR01T').text
        phn_cong = res.find('div',class_='fMghEO').text
        phn_price = res.find('div',class_='_30jeq3 _1_WHN1').text
        actual_price = res.find('div',class_ = '_3I9_wc _27UcVY').text
        link = res.a['href']
       
       #To print details of phone
        print()
        print(f"PHONE NAME --> {phn_name.strip()}")
        print(f"CONFIGURATION --> {phn_cong.strip()}")
        print(f"PRODUCT PRICE --> {actual_price.strip()}")
        print(f"OFFER PRICE --> {phn_price.strip()}")
        print("LINK --> https://www.flipkart.com"+link)

#Runs after every 10 minutes
if __name__ == '__main__':
    while True:
        find_phone()
        time_wait = 10
        print(f'\nWating for {time_wait} minutes ....')
        time.sleep(time_wait*60)
