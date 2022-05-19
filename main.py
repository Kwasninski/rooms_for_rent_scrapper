from re import L
import requests
from bs4 import BeautifulSoup

import pandas as pd



def extract(page):

    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
    url = f'https://www.otodom.pl/pl/oferty/wynajem/pokoj/warszawa?priceMax=1600&page={page}&limit=72'

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')
    return soup



def transform(soup):
    divs = soup.find_all('li', class_ = 'css-p74l73 es62z2j17')
    for item in divs:

        title = item.find('h3', class_='css-1rhznz4 es62z2j11').text.strip()

        price = item.find('span', class_='css-rmqm02 eclomwz0').text.strip()

        try:
            location_add_date = item.find('span', class_='css-17o293g es62z2j9').text.strip()
        except:
            location_add_date = ''

        for link in item.find_all('a', href=True):
            full_link = ('otodom.pl'+link['href'])  


        room = {
            'Nazwa Oferty': title,
            'Cena': price,
            'Lokalizacja': location_add_date,
            'Link': full_link
        }
        room_list.append(room)
    return





room_list = []
for i in range(1):

    c = extract(0)
    transform(c)
print(len(room_list))



df = pd.DataFrame(room_list)

print(df.head())

df.to_csv('rooms.csv')

