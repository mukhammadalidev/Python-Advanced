
class Product:
    def __init__(self, name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    
    def get_info(self):
        return f"name:{self.name} price:{self.price} quantity:{self.quantity}"
    



product1 = Product('Muhammad',4000,4)
print(product1.get_info())



class Cart:
    def __init__(self):
        self.products = []

    
    def add_product(self,product:Product):
        self.products.append(product)
        
        return f"{product.name} savatga qo'shildi ➕"


    def show_product(self):
        for product in self.products:
            return product.get_info()
    

    def get_total_price(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
            return total 
    


cart = Cart()
cart.add_product(product1)
print(cart.get_total_price())