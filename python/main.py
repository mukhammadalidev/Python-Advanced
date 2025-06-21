class Base:
    def __init__(self,name,age):
        self.name = name
        self.age = age



class Student(Base):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id = id

    
    def greeting(self):
        return f"name:{self.name} age:{self.age} id:{self.id}"
    




student1 = Student('Ali',15,123456)

print(student1.greeting())




class BankHisobi:
    def __init__(self, balans):
        self.__balans = balans  # private o'zgaruvchi

    def get_balance(self):
        return self.__balans

    def set_balance(self, new_balance: int):
        if new_balance >= 0:
            self.__balans = new_balance
        else:
            print("Xatolik: balans manfiy bo‘lishi mumkin emas")

    def hisob_info(self):
        return f"Hozirgi balans: {self.__balans} so'm"


hisob1 = BankHisobi(1000)

# to‘g‘ri usulda o‘zgartirish
hisob1.set_balance(5000)

# noto‘g‘ri urinish - bu hech narsani o‘zgartirmaydi
hisob1.__balans = 999999

print(hisob1.hisob_info())         # 5000
print(hisob1.get_balance())        # 5000
print(hisob1.__balans)             # 999999 (lekin bu boshqa obyekt ichidagi emas!)
