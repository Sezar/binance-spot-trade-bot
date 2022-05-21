from binance.client import Client
import binanceClass
import algorithmClass
import time
import datetime

apiKey = "APIKEY"
secretKey = "SECRETKEY"
client = Client(apiKey, secretKey)

coinName="BTC"
roud = 5

COIN = binanceClass.bClass(coinName+"USDT",coinName,roud,apiKey,secretKey)

while True:
    COIN.cagir()
    time.sleep(10)