class Hero: #Родительский класс
    def __init__(self, name, age, damage, armor, health):
        self.name = name # Атрибуты
        self.age = age
        self.damage = damage
        self.armor = armor
        self.health = health
    
    def person(self):
        print(f"Имя {self.name}, Возраст {self.age}")

    def fight(self):
        print(f"Сила - {self.damage}\nБроня - {self.armor}\nЗдоровье - {self.health}")

    def info(self):
        print(f"\nИмя - {self.name}\nВозраст - {self.age}\nСила - {self.damage}\nБроня - {self.armor}\nЗдоровье - {self.health}")
        

dima = Hero('Демон', 78, 80, 30, 220)
frank = Hero('Громила', 20, 95, 10, 330)


dima.info()
frank.info()

dima.health = dima.health - frank.damage
dima.health
dima.info()




