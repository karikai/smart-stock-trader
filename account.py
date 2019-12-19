import transaction as TRA
import fbconnector as FIRE

class Account:
    capital = 0
    accountID = ''
    stocks = []
    transactions = []
    shares = []
    
    def __init(self):
        self.capital = 0
        self.stocks = []
        self.transactions = []
        self.accountID = ''

    def initializeAccount(self, capital, stocks, transactions, accountID):
        self.capital = capital
        self.stocks = stocks
        self.transactions = transactions
        self.accountID = accountID

    def buy(self, stock, quantity):
        print('Bought: ' + str(quantity) + ' - ' + stock['symbol'])
        newTransaction = TRA.Transaction()
        newTransaction = newTransaction.createBuyTransaction(stock, quantity)
        if (self.canMakeTransaction(newTransaction.calculateTotal())):
            TRA.Transaction.buy(newTransaction, self)
        else:
            print('Not enough capital')

    def sell(self, stock, quantity):
        print('Sold: ' + str(quantity) + ' - ' + stock['symbol'])
        newTransaction = TRA.Transaction()
        newTransaction = newTransaction.createSellTransaction(stock, quantity)
        print(self.getShareIndices(stock['symbol']))
        TRA.Transaction.sell(newTransaction, self, self.getShareIndices(stock['symbol']))

    def getCapital(self):
        total = 0
        for transaction in self.transactions:
            total += transaction.stock['latestPrice']
        return self.capital + total

    def canMakeTransaction(self, transactionAmount):
        if ((transactionAmount * -1) <= self.capital):
            return True
        else:
            return False

    def getSharesBySymbol(self, symbol):
        currentShares = []
        for share in self.shares:
            if (share.symbol.lower() == symbol.lower()):
                currentShares.append(share)
        return currentShares

    def getShareIndices(self, symbol):
        indices = []    
        index = 0
        for share in self.shares:
            if (share.symbol.lower() == symbol.lower()):
                indices.append(index)
            index += 1
        print(indices)
        return indices

    def ownsShare(self, symbol):
        check = False
        for share in self.shares:
            if (share.symbol.lower() == symbol.lower()):
                check = True
        return check
