class Share:
    symbol = None
    orderDate = None
    originalPrice = None

    def __init__(self, stock, orderDate):
        self.symbol = stock['symbol']
        self.orderDate = orderDate
        self.originalPrice = stock['latestPrice']

