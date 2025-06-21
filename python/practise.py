


class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email


    
    def get_info(self):
        print(f"name:{self.name} email:{self.email}")
    



class Admin(User):
    def __init__(self, name, email,role):
        super().__init__(name, email)
        self.role = role

    def get_info(self):
        print(f"name:{self.name} email:{self.email} role:{self.role}")

    

user1 = User("Muhammad","mukhammadalidev@gmail.com")
admin1 = Admin("Admin","ali@gmail.com",'admin')
user1.get_info()
admin1.get_info()

class BankAccount(User):
    def __init__(self,balance,name,email):
        super().__init__(name,email)
        self.__balance = balance

    

    def get_info(self):
        return f"name:{self.name} email:{self.email} count:{self.__balance}"
    
    def deposit(self,deposit:int):
        if self.__balance > 0:
            self.__balance += deposit
            return "Balans To'ldirildi"
        else:
            return "Xato"
    

    def withdraw(self,withdraw:int):
        if self.__balance > 0:
            self.__balance -= withdraw
            return f"{self.__balance} qoldi"
        else:
            return "Xato"    

account = BankAccount(name='Muhammadali',email='mukhammadalidev@gmail.com',balance=4000)
print(account.get_info())
print(account.withdraw(2000))



