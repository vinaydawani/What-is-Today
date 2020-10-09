import rumps
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://nationaltoday.com/what-is-today/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')