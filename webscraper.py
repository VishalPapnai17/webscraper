import time
import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/boAt-Heads-225-Headphones-Button/dp/B01MCUSD3L/ref=sr_1_8?keywords=boat+earphones&qid=1562307805&s=gateway&sr=8-8"

headers = { "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def checkprice():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')


 
    price = soup.find(id = "priceblock_ourprice").get_text()
    integral_price = float(price[1:5])
    if (integral_price<600):
        mail_me()
def mail_me():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('vishalpapnai2000@gmail.com','lmzpgntqjcxeowfr')

    subject = "price fell down"
    body = "check the amazon link https://www.amazon.in/boAt-Heads-225-Headphones-Button/dp/B01MCUSD3L/ref=sr_1_8?keywords=boat+earphones&qid=1562307805&s=gateway&sr=8-8"
    message = "subject: {} \n\n\n\n {}".format(subject,body) 
    server.sendmail(
        'vishalpapnai2000@gmail.com',
        'ekanshisharma1998@gmail.com',
        message      )
    print('Hey,email has been sent')
    
    server.quit()


while True:
        checkprice()
