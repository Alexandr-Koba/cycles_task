def twice_func(inside_func):
   """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
   inside_func()
   inside_func()

def hello():
   print("Привет")
  
test = twice_func(hello)
