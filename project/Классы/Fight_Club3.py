class Hero: #Родительский класс
    def __init__(self, name, age, damage, armor, health):
        self.name = name        # Атрибуты
        self.age = age          # Атрибуты
        self.damage = damage    # Атрибуты
        self.armor = armor      # Атрибуты
        self.health = health    # Атрибуты
    
    def person(self): # Метод имя возраст
        print(f"Имя {self.name}, Возраст {self.age}")

    def fight(self):  # Метод сила, броня, Здоровье
        print(f"Сила - {self.damage}\nБроня - {self.armor}\nЗдоровье - {self.health}")

    def info(self): # Метод вывода инфо
        print(f"\nИмя - {self.name}\nВозраст - {self.age}\nСила - {self.damage}\nБроня - {self.armor}\nЗдоровье - {self.health}")

class Monster(Hero): # Потомок (Наследование) 
    def __init__(self, name, age, damage, armor, health, spec):
        super().__init__(self, name, age, damage, armor, health)
        self.spec = spec
    
    def info(self):
        print(f"\nИмя - {self.name}\nВозраст - {self.age}\nСила - {self.damage}\nБроня - {self.armor}\nЗдоровье - {self.health}\n Спец - {self.spec}")




dima = Hero('Демон', 78, 80, 30, 220)
frank = Hero('Громила', 20, 95, 10, 330)

pig = Monster('Громила', 1, 25, 20, 110, 5)
pig.info()

pig.info()
dima.info()
frank.info()