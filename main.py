import requests
from bs4 import BeautifulSoup
import mysql.connector

def save_to_mysql(title, price, mileage):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="your pass", #pls enter your database pass
        database="divar_ads"
    )
    cursor = conn.cursor()
    query = "INSERT INTO ads (title, price, mileage) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, price, mileage))
    conn.commit()
    cursor.close()
    conn.close()

def get_divar_ads():
    url = "https://divar.ir/s/tehran/car"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    }

    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    ads = soup.find_all("div", class_="unsafe-kt-post-card__info")

    for ad in ads[6:15]:
        title_tag = ad.find("h2")
        info = ad.find_all("div", class_="unsafe-kt-post-card__description")
        
        title = title_tag.text.strip() if title_tag else "unknown"
        price = info[1].text.strip() if len(info) > 1 else "unknown"
        mileage = info[0].text.strip() if info else "unknown"
        print("🏎️ عنوان:", title)
        print("💰 قیمت:", price)
        print("📍 کارکرد:", mileage)
        print("-" * 40)

        
        save_to_mysql(title, price, mileage)

get_divar_ads()