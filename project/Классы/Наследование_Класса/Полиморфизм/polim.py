
class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b		  
    
    def get_area(self):		
        return self.a * self.b
    
    def show(self):
        print(f"{self.a} * {self.b} = {self.a * self.b}")

class Square:
    def __init__(a):
    self.a = a
    
    def get_area_square(self):		
        return self.a ** 2

    def show(self):
        print(f"{self.a} ** 2 = {self.a**2}")
#возведение в степень **2 (в квадрат)

