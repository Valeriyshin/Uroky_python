# class Product:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
    
#     def info(self):
#         print("Название: ",  self.title, "Цена: ", self.price, "тг")
    
# laptop = Product("Asus", 600000)
# iphone = Product("Iphone 17", 700000)
# laptop.info()
# iphone.info()








class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.__hp = hp
        self.damage = damage
        self.inventory = []
        
    def info(self):
        print("Имя: ", self.name, "| HP: ", self.__hp, "| Урон: ", self.damage)
        
    def take_damage(self, dmg):
        if dmg < 0:
            return
        self.__hp -=dmg
        if self.__hp < 0:
            self.__hp = 0
            
    def heal(self, amount):
        if amount <0:
            return
        self.__hp += amount
        print(self.name, "лечиться на: ", amount)
        if self.__hp >100:
            self.__hp = 100
            
    def attack(self, target):
        print(self.name, "бьет", target.name, "на", self.damage)
        target.take_damage(self.damage)
        
    def add_item(self, item):
        self.inventory.append(item)
        print(self.name, "Получил предмет: ", item.name)
        
    def show_inventory(self):
        if (self.inventory) == 0:
            print(self.name, "Инвентарь пуст")
            return
        print("Инвентарь", self.name + ":")
        for i, item in enumerate(self.inventory, start = 1):
            print(i, "-", item.name)
            
    def use_item(self, item_index, target = None):
        if item_index < 1 or item_index > len(self.inventory):
            print("Нет предмета под таким номером")
            return
        item = self.inventory.pop(item_index - 1)
        item.apply(user = self, target = target)

    def is_alive(self):
        return self.__hp > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 150, 20)
        
    def attack(self, target):
        print(self.name, "рубит мечом", target.name, "на", self.damage)
        target.take_damage(self.damage)
      
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80, 30)
        self.mana = 100
        
    def cast_spell(self, target):
        if self.mana < 20:
            print(self.name, "не хватает маны")
            return
        self.mana -=20
        print(self.name, "кастует фаербол")
        target.take_damage(self.damage + 10)

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, 120, 18)
        
    def heal_ally(self, target):
        if not target.is_alive():
            print(target.name, "Уже мертв, лечить нельзя")
            return
        
        print(self.name, "лечит союзника", target.name)
        target.heal(25)
        
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, 90, 25)
        self.energy = 100
        
    def attack(self, target):
        print(self.name, "Атакует", target.name, "на", self.damage)
        target.take_damage(self.damage)
        
    def backstab(self, target):
        if self.energy < 30:
            print (self.name, "Недостаточно стамины")
            return
        self.energy -=30
        print(self.name, "Атакует со спины", target.name, "на", self.damage*2)
        target.take_damage(self.damage*2)
           
class Item:
    def __init__(self, name):
        self.name = name
        
    def apply(self, user, target = None):
        raise NotImplementedError("Нужно переопределить apply() в наследники")
    
class Potion(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name)
        self.heal_amount = heal_amount
        
    def apply(self, user, target=None):
        if target is None:
            target = user
        
        print(user.name, "использует", self.name, "на", target.name)
        target.heal(self.heal_amount)
    
class Bomb(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage
    
    def apply(self, user, target = None):
        if target is None:
            print("Нужно указать цель для бомбы")
            return
        
        print(user.name, "боосает", self.name, "в", target.name)
        target.take_damage(self.damage)  
     
war = Warrior("Тралл")
mage = Mage("Джайна")
pal = Paladin("Артас")
rog = Rogue("Валира")

pal.add_item(Potion("Малая банка хила", 20))
pal.add_item(Potion("Бальшая банка хила", 50))
pal.add_item(Bomb("Святая граната", 30))

pal.show_inventory()

turn = 1

while war.is_alive() and mage.is_alive():
    print("\n--- Ход", turn, "---")
    
    war.attack(mage)
    mage.attack(war)
            
    if turn == 1:
        pal.heal_ally(mage)
        rog.backstab(mage)
    elif turn == 2:
        pal.use_item(1, target = mage)
        rog.backstab(war)
    elif turn == 3:
        pal.use_item(1, target= mage)
        
    else:
        pal.use_item(1, target=war)
        
    war.info()
    mage.info()
    
    if not mage.is_alive():
        break
    if not war.is_alive():
        break
        
    turn +=1
    if turn>6:
        break

# war.attack(mage)
# mage.info()

# mage.cast_spell(war)
# war.info()      


# orc.info()
# human.info()
# orc.attack(human)
# human.info()

# human.heal(5)
# human.info()




# # Инкапсуляция
# . -> публичный, можно менять как угодно
# _ -> protected, не трогай снаружи, это внутреннее
# __ -> приватный, Python -> name manling, прямого доступа нет