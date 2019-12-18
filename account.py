import transaction as TRA

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
        newTransaction = TRA.Transaction()
        newTransaction = newTransaction.createBuyTransaction(stock,quantity)
        if (self.canMakeTransaction(newTransaction.calculateTotal())):
            TRA.Transaction.buy(newTransaction, self)
        else:
            print('Not enough capital')

    # def sell(self, stock, quantity):
    #     newTransaction = transaction.Transaction()
    #     newTransaction = newTransaction.createSellTransaction(stock,quantity)
    #     if (self.canMakeTransaction(newTransaction.calculateTotal())):
    #         self.transactions.append(newTransaction)
    #     else:
    #         print('Not enough capital')

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
