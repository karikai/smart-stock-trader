import requests
import json
import time
import account


class SST:
    account = None
    SSTConfig = None

    def __init__(self, account, config):
        self.account = account
        self.SSTConfig = config

    def getStock(self, symbol):
        request = 'https://cloud.iexapis.com/stable/stock/' + symbol + '/quote?token=pk_fc4857bc809645fb98c7bfa9132d259d'
        return request

    ## Presents JSON from API in a user-friendly format
    def jsonToStock(self, jsonObj):
        stockDict = json.loads(jsonObj)
        return stockDict

    def initiateBuy(self):
        return True

    # def initiateSell(self):


    def watch(self):
        while True:
            for stock in self.account.stocks:
                stockResponse = requests.get(self.getStock(stock))
                stockObject = self.jsonToStock(stockResponse.content)
                print(stockObject['symbol'],stockObject['latestPrice'])
                if (self.initiateBuy()):
                    self.account.buy(stockObject, 5)
                print(self.account.capital) 
                
            time.sleep(self.SSTConfig.latency)

