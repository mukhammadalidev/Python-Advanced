from models.order import Order


class OrderService:
    def __init__(self):
        self.orders = []

    
    def create_order(self,user):
        if not user.cart:
            raise Exception("Savat Bo'sh aval Mahsulot Qo'shing")
        
        order = Order(user,user.cart.copy())
        self.orders.append(order)
        user.cart.clear()
        return order