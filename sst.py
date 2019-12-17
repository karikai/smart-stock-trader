import requests
import json
import time
import account


class SST:
    account = None
    SSTConfig = None

    def __init__(self):
        self.account = account.Account()
        self.SSTConfig = None

    def getStock(self, symbol):
        request = 'https://cloud.iexapis.com/stable/stock/' + symbol + '/quote?token=pk_fc4857bc809645fb98c7bfa9132d259d'
        return request

    ## Presents JSON from API in a user-friendly format
    def jsonToStock(self, jsonObj):
        stockDict = json.loads(jsonObj)
        return stockDict

    def watch(self):
        while True:
            for stock in self.account.stocks:
                stockResponse = requests.get(self.getStock(stock.symbol))
                stockObject = self.jsonToStock(stockResponse.content)
                
                time.sleep(self.SSTConfig.latency)

