# Инкапсуляция
# 1) _ Первый уровень защиты
# 2) __ Второй уровень защиты

class Car(): # Родитель
    def __init__(self, brand, color): # Метод Конструктор определяет атрибуты
        self.brand = brand
        self.color = color
    
    def show(self): # Метод — это всего лишь функция, реализованная внутри класса, и первым аргументом принимающая self:
        print(f"{self.brand} {self.color}")

class Bus(Car): # Патомок
    def __init__(self, brand, color, count):
        super().__init__(brand, color)
        self.count = count

    def __show(self): # Метод — это всего лишь функция, реализованная внутри класса, и первым аргументом принимающая self:
        print(f"{self.brand} {self.color}. Колл-во мест: {self.count}") #Полиморфизм (переопределение метода класса)


car1 = Car('BMW', 'RED')
car1.show()

bus1 = Bus('Паз', 'Белый', 40)
bus1.show()



