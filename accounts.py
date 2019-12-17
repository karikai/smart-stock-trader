import transactions

class Account:
    capital = 0
    accountID = ''
    stocks = []
    transactions = []

    def __init__(self, capital, stocks, transactions, accountID):
        self.capital = capital
        self.stocks = stocks
        self.transactions = transactions
        self.accountID = accountID
    
    def __init(self):
        self.capital = 0
        self.stocks = []
        self.transactions = []
        self.accountID = ''

    def buy(self, stock, quantity):
        newTransaction = transactions.Transaction()
        newTransaction = newTransaction.createBuy(stock,quantity)
        if (self.canMakeTransaction(newTransaction.calculateTotal())):
            self.transactions.append(newTransaction)
        else:
            print('Not enough capital')


    def sell(self, stock, quantity):
        newTransaction = transactions.Transaction()
        newTransaction = newTransaction.createSell(stock,quantity)
        if (self.canMakeTransaction(newTransaction.calculateTotal())):
            self.transactions.append(newTransaction)
        else:
            print('Not enough capital')

    def getCapital(self):
        total = 0
        for transaction in self.transactions:
            total += transaction.stock['latestPrice']
        return self.capital + total

    def canMakeTransaction(self, transaction):
        if (transaction.calculateTotal() <= self.capital):
            return True
        else:
            return False
