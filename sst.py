import requests
import json
import time
import account
import random


class SST:
    account = None
    SSTConfig = None
    runtime = None
    floatingStopGain = None
    floatingStopLoss = None

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

    def initiateBuy(self, stock):
        # logic for initiating buy
        # if stock['isUSMarketOpen']:
        #     if (stock['latestPrice'] <= (1.1 * stock['low'])): # Checks to see if stock price is 10% within its daily low
        #         return True
        #     else:
        #         return False            
        # else:
        #     return False
        val = True if (random.randint(1,101) > 80) else False
        return val

    # def determineBuyAmount(self):

    def initiateSell(self, stock):
        # logic for initiating sell
        # if stock['isUSMarketOpen']:
        #     investmentTotal = 0
        #     net = 0

        #     for share in self.account.getSharesBySymbol(stock['symbol']):
        #         investmentTotal += share.originalPrice
        #         net += share.originalPrice - stock['latestPrice']
            
        #     # Stop Gain
        #     if net >= investmentTotal * .05: # Stops gains at 5% of initial investment
        #         return True
        #     # Stop Loss
        #     elif net <= investmentTotal * -.05: # Stops losses at 5% of initial investment
        #         return True
        #     else:
        #         return False
        # else:
        #     return False
        if self.account.ownsShare(stock['symbol']):
            val = True if (random.randint(1,101) > 80) else False
            return val

    # def determineSellAmount(self):

    def watch(self):
        self.runtime = 0
        while True:
            for stock in self.account.stocks:
                stockResponse = requests.get(self.getStock(stock))
                stockObject = self.jsonToStock(stockResponse.content)
                print(stockObject['symbol'],stockObject['latestPrice'])
                if (self.initiateBuy(stockObject)):
                    self.account.buy(stockObject, 5) 
                if (self.initiateSell(stockObject)):
                    self.account.sell(stockObject, len(self.account.getSharesBySymbol(stock['symbol'])))

            print(self.account.shares)    
            time.sleep(self.SSTConfig.latency)
            

