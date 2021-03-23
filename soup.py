from bs4 import BeautifulSoup
import requests

URL = "https://coinmarketcap.com/currencies/bitcoin/historical-data/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

able = soup.find_all('table')

print(able)