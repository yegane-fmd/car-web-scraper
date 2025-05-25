import requests
from bs4 import BeautifulSoup
import mysql.connector

res = requests.get("https://rojashop.com/shop/cosmetic")

soup = BeautifulSoup(res.text , 'html.parser')

print(soup.find_all('a' , attrs={}))