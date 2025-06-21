class User:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    
class BankHisob(User):
    def __init__(self, name,balance, id):
        super().__init__(name, id)
        self.__balance = balance
    
    def get_balance(self):
        print(self.__balance)
    
    def deposit(self,amount:int):
        if self.__balance > 0:
            self.__balance += amount
            print("Malumot chop etildi")
        else:
            print("Xatolik yuz berdi")
    def withdraw(self,amount:int):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print('pul muffaqiyatli yechildi')
        else:
            print('Xatolik yuz berdi pul chiqarishda!!')
    
    def info(self):
        print(f"{self.name} {self.id} {self.__balance}")


ali = BankHisob(name='Ali',id=123,balance=5000,withdraw=3000,deposit=1500)
ali.withdraw(3000)
ali.info()