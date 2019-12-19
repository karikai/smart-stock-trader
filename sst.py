# pylint: disable=import-error
import requests
import json
import time
import account as ACT
import sstconfig as CONFIG
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
        if not self.account.ownsShare(stock['symbol']):
            if stock['isUSMarketOpen']:
                if (stock['latestPrice'] <= (stock['previousClose'])): # Checks to see if stock price is less than previous close
                    return True
                else:
                    return False
            else:
                return False            
        else:
            return False

    # def determineBuyAmount(self):

    def initiateSell(self, stock):
        # logic for initiating sell
        if self.account.ownsShare(stock['symbol']):
            if stock['isUSMarketOpen']:
                investmentTotal = 0
                net = 0

                for share in self.account.getSharesBySymbol(stock['symbol']):
                    investmentTotal += share.originalPrice
                    net += share.originalPrice - stock['latestPrice']
                
                # Stop Gain
                if net >= investmentTotal * .05: # Stops gains at 5% of initial investment
                    return True
                # Stop Loss
                elif net <= investmentTotal * -.05: # Stops losses at 5% of initial investment
                    return True
                else:
                    return False
        else:
            return False

    # def determineSellAmount(self):

    def watch(self):
        print('Your Balance: $' + str(self.account.capital))
        print('You\'re Watching: ' + self.account.echoStocks())
        print('SST will refresh stocks quotes every ' + str(self.SSTConfig.latency) + ' seconds.')
        while True:
            for stock in self.account.stocks:
                stockResponse = requests.get(self.getStock(stock))
                stockObject = self.jsonToStock(stockResponse.content)
                print(stockObject['symbol'],stockObject['latestPrice'])
                if (self.initiateBuy(stockObject)):
                    self.account.buy(stockObject, 5)
                    print(str(self.account.capital))
                if (self.initiateSell(stockObject)):
                    self.account.sell(stockObject, self.account.getShareAmount(stockObject['symbol']))
                    print(str(self.account.capital))

            print(self.account.shares)    
            time.sleep(self.SSTConfig.latency)
            

