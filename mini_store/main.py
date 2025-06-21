from models.products import Product
from models.user import User
from services.order_service import OrderService


user = User("Ali")
p1 = Product("Olma",4000)
p2 = Product("Non",400)

user.add_to_cart(p1)
user.add_to_cart(p2)

service = OrderService()
order = service.create_order(user)

# Natijani chiqaramiz
print(f"{order.user.username} buyurtmasi umumiy: {order.total()} so'm")