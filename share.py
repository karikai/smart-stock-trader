class Share:
    symbol = None
    orderDate = None
    stock = None
    originalPrice = None

    def __init__(self, stock, orderDate):
        self.symbol = stock['symbol']
        self.stock = stock
        self.orderDate = orderDate
        self.originalPrice = stock['latestPrice']

