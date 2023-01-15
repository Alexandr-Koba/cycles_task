class Car(): # Родитель
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def show(self):
        print(f"{self.brand} {self.color}")

class Bus(Car): # Патомок
    def __init__(self, brand, color, count):
        super().__init__(brand, color)
        self.count = count

    def show(self):
        print(f"{self.brand} {self.color}. Колл-во мест: {self.count}") #Полиморфизм (переопределение метода класса)


car1 = Car('BMW', 'RED')
car1.show()

car1.brand = "Mers"
car1.show()

bus1 = Bus('Паз', 'Белый', 40)
bus1.show()
