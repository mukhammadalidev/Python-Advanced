class Order:

    def __init__(self,user,product):
        self.user = user
        self.product = product

    
    def total(self):
        return sum([p.price for p in self.product])