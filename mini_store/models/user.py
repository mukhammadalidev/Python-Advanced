class User:
    def __init__(self,username):
        self.username = username
        self.cart = []

    
    def add_to_cart(self,product):
        self.cart.append(product)
    

    def get_total_cart(self):
        return sum([p.price for p in self.cart])