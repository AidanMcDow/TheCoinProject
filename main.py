import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/historical/20210207/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(class_='cmc-main-section')

prices = table.find_all('td', 'cmc-table__cell--sort-by__price')
for price in prices:
    print(price.text, end='\n')

