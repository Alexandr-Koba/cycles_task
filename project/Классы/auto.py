#Наследование

class Car(): # Родитель
    def __init__(self, brand, color):
        self.brand = brand # Атрибуты
        self.color = color # Атрибуты
    
    def show(self):
        print(f"{self.brand} {self.color}")
    

class Bus(Car): # Потомок
    def __init__(self, brand, color, count):
        super().__init__(brand, color)
        self.count = count # Добавил новый атрибут к дополнению к родительских атрибутам

    def show(self):
        print(f"{self.brand} {self.color} Вмещает: {self.count} чловек")

car1 = Car("BMW", "Green")
car1.show()

bus1 = Bus("Паз", "Белый", 40)
bus1.show()