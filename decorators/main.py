class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


# Obyektlar yaratamiz
u1 = User("Ali")
u2 = User("Vali")
u3 = User("Sami")

# Umumiy foydalanuvchilar sonini ko‘ramiz
print(User.get_count())  # ➜ 3