# Задание 1. Timer
# Создать класс Timer:
# - атрибут seconds (начально 0)
# - методы:
#   add(value) — прибавляет секунды
#   reset() — сбрасывает в 0
#   get_time() — возвращает строку mm:ss

# Пример: 65 секунд → 01:05

class Timer:
    def __init__(self):
        self.seconds = 0

    def add(self, value):
        self.seconds += value

    def reset(self):
        self.seconds = 0

    def get_time(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        return f"{minutes:02}:{seconds:02}"
    
get_time = Timer()
get_time.add(90)
print(get_time.get_time())

# Задание 2. Playlist
# Создать класс Playlist:
# - songs (список песен)
# - методы:
#   add_song(title)
#   remove_song(title)
#   count()
#   show()
class Playlist:
    def __init__(self):
        self.songs = []
    def add_song(self, title):
        self.songs.append(title)
    def remove_song(self, title):
        if title in self.songs:
            self.songs.remove(title)
    def count(self):
        return len(self.songs)
    def show(self):
        return self.songs
my_playlist = Playlist()
my_playlist.add_song("Song 1")
my_playlist.add_song("Song 2")
print(my_playlist.show())
print(my_playlist.count())

# Задание 3. ShopCart
# Создать класс ShopCart:
# - items — список объектов Product
# - методы:
#   add_product(product)
#   remove_product_by_name(name)
#   get_total()

# Использовать класс Product:
# - name, price, quantity
# - get_total_price()
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity   
    
class ShopCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product_by_name(self, name):
        self.items = [item for item in self.items if item.name != name]

    def get_total(self):
        return sum(item.get_total_price() for item in self.items)
cart = ShopCart()
product1 = Product("Apple", 200, 5)
product2 = Product("Banana", 100, 10)
cart.add_product(product1)
cart.add_product(product2)
print(cart.get_total())

# Задание 4. SafeBankAccount
# Создать класс SafeBankAccount:
# - owner, balance
# - методы:
#   deposit(amount > 0)
#   withdraw(amount > 0 и <= balance)
#   get_balance()

# Если сумма некорректна — выводить 'Ошибка'.

class SafeBankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Ошибка")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Ошибка")

    def get_balance(self):
        return self.balance
    
Kaspi = SafeBankAccount("Ivan", 10000)
Kaspi.deposit(5000)
Kaspi.withdraw(2000)
print(Kaspi.get_balance())
Kaspi.withdraw(20000) 
