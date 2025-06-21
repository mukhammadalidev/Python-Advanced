# init eq repr add str 

# str
class Product:
    def __init__(self,name,quantity,price):
        self.name = name
        self.price = price
        self.quantity = quantity


    def __add__(self,other):
        if self.name == other.name and self.price == other.price:
            new_quantity = self.quantity + other.quantity
            return Product(self.name,self.quantity,new_quantity)
        else:
            raise ValueError("Nom yoki narx mos emas — qo‘sha olmaysiz.")
        # bu methods  2ta obyektni tenglashtirish uchun yoziladi
    def __eq__(self, value):
        return (self.quantity == value.quantity and self.name == value.name and self.price == value.price) 

    def __str__(self):#bu methods print funksiyasi bilan ishlaydi
        return f"name:{self.name} - {self.price}"
    
p1 = Product('Muhammadali',3,3000)
p2 = Product('Muhammadali',3,3000)

p3 = p1+p2
p4 = (p1 == p2)

# __str__
print(p4)


