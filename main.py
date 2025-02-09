from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import time
app = Flask(__name__)

def getgold():
  url = "https://saatchico.com/calculator#"
  
  # ارسال درخواست به سایت
  response = requests.get(url)
  
  # پارس کردن محتوای HTML
  soup = BeautifulSoup(response.content, "html.parser")
  
  # جستجو برای قیمت طلا با استفاده از کلاس text-bold
  gold_price = soup.find("span", class_="text-bold").text
  
  return gold_price



def gettet():
  api = requests.get('https://api.nobitex.ir/v3/orderbook/USDTIRT')

  res = api.json()

  lastp = res.get('lastTradePrice')
  
  return lastp


def getprice(currency_type):
    api_key = '7519195d-c61d-49ed-8213-66b3b97a4022'
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        'symbol': currency_type,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    if response.status_code == 200:
        currency_data = data['data'][currency_type]
        price = currency_data['quote']['USD']['price']
        percent_change_24h = currency_data['quote']['USD']['percent_change_24h']
        rank = currency_data['cmc_rank']


        return round(price,3)

@app.route('/')
def index():
    tether = gettet()
    time.sleep(0.01)
    BTC = getprice('BTC')
    time.sleep(0.01)
    TON = getprice('TON')
    time.sleep(0.01)
    TRX = getprice('TRX')
    time.sleep(0.01)
    GOLDUSD = getprice('XAUt')
    time.sleep(0.01)
    GOLD=getgold()
    return render_template('index.html',BTC=BTC,TRX=TRX,TON=TON,tether=tether,GOLD=GOLD,GOLDUSD=GOLDUSD)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)