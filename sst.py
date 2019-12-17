import requests
import json
import time

class SST:
    # def __init__(self):
        # self.account = none
        # self.sstConfig = none

    def getStock(self, symbol):
        request = 'https://cloud.iexapis.com/stable/stock/' + symbol + '/quote?token=pk_fc4857bc809645fb98c7bfa9132d259d'
        return request

    ## Presents JSON from API in a user-friendly format
    def jsonToStock(self, jsonObj):
        stockDict = json.loads(jsonObj)
        return stockDict

    def watch(self):
        while True:
            for stocks in self.account.stocks
            stockResponse = requests.get(self.getStock("F"))
            stockObject = self.jsonToStock(stockResponse.content)
            time.sleep(2)

