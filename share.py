class Share:
    symbol = None
    quantity = None
    orderDate = None
    stock = None

    def __init__(self, stock, quantity, orderDate):
        self.symbol = stock.symbol
        self.stock = stock
        self.orderDate = orderDate
        self.quantity = quantity

