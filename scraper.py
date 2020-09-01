import requests
from bs4 import BeautifulSoup

oyo_url = "https://www.oyorooms,com/hotels-in-bangalore/"

req = requests.get(oyo_url)
content = req.content
