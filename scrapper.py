import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/SanDisk-Class-Memory-Adapter-SDSQUAR-032G-GN6MA/dp/B073JWXGNT/ref=sr_1_2?crid=29AIKAQJYRIFO&keywords=sd+card+64+gb&qid=1573147058&s=electronics&sprefix=sd+card%2Celectronics%2C368&sr=1-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:5])

    
    print(converted_price)
    print(title.strip())

    if(converted_price < 400):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('arodirohit2@gmail.com' , 'yjofwdvzkrlrovus')

    subject = "Hey the price fell down"
    body = "Check the amazon link https://www.amazon.in/SanDisk-Class-Memory-Adapter-SDSQUAR-032G-GN6MA/dp/B073JWXGNT/ref=sr_1_2?crid=29AIKAQJYRIFO&keywords=sd+card+64+gb&qid=1573147058&s=electronics&sprefix=sd+card%2Celectronics%2C368&sr=1-2"

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'arodirohit2@gmail.com',
        'iknowlittlecode@gmail.com',
        msg
    )
    print("HEY THE EMAIL HAS BEEN SENT !")

    server.quit()

check_price()