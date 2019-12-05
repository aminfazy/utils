import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.iitp.ac.in/'
headers = {
	"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}

page = requests.get(URL, headers)
soup = bs(page.content, 'html.parser')
# print(soup)
price = soup.find(id = "info").get_text()
# converted_price = float(price[0:4])
# print(converted_price)
print(price.strip())