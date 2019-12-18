import datetime
import share

class Transaction:
    stock = None
    quantity = None
    transactionType = None
    date = None

    def create(self, stock, quantity):
        self.date = datetime.datetime.now()
        self.stock = stock
        self.quantity = quantity

    def createBuyTransaction(self, stock, quantity):
        self.create(stock, quantity)
        self.type = 'buy'
        return self

    def createSellTransaction(self, stock, quantity):
        self.create(stock, quantity)
        self.type = 'sell'
        return self

    def calculateTotal(self):
        if self.transactionType == 'sell':
            return self.stock['latestPrice'] * self.quantity
        else:
            return (self.stock['latestPrice'] * self.quantity) * -1

    @staticmethod
    def createShare(transaction):
        return share.Share(transaction.stock, transaction.date)

    @staticmethod
    def buy(newTransaction, account):
        if newTransaction.quantity is not 0:
            account.transactions.append(newTransaction)
            if (newTransaction.quantity > 1):
                i = 0
                while i < newTransaction.quantity:
                    account.shares.append(Transaction.createShare(newTransaction))
                    account.capital -= newTransaction.stock['latestPrice']
                    i += 1
                    print(i, newTransaction.stock['latestPrice'])
            if (newTransaction.quantity == 1):
                account.shares.append(Transaction.createShare(newTransaction))
                account.capital -= newTransaction.stock['latestPrice']

    # @staticmethod
    # def sell(newTransaction, account, indicies):
    #     shareAmount = account.getNumberOfShares(newTransaction.stock.symbol n)


