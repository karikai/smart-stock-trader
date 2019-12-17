import datetime

class Transaction:
    stock = None
    quantity = None
    transactionType = None
    accompanyingTransaction = None
    date = None

    def create(self, stock, quantity):
        self.date = datetime.datetime.now()
        self.stock = stock
        self.quantity = quantity

    def createBuy(self, stock, quantity):
        self.create(stock, quantity)
        self.type = 'buy'
        return self

    def createSell(self, stock, quantity):
        self.create(stock, quantity)
        self.type = 'sell'
        return self

    def exitTransaction(self, transaction):
        self.accompanyingTransaction = transaction

    def calculateTotal(self):
        if self.transactionType == 'sell':
            return self.stock['latestPrice'] * self.quantity
        else:
            return (self.stock['latestPrice'] * self.quantity) * -1