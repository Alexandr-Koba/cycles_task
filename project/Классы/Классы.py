
class Exemple:
    def car(brand, color):
        return brand, color

    def driver(name):
        return name

    def info(name, brand, color):
        res = f'У {name} есть {color} {brand}'
        return res

    def test():
        print('Работает')


x = Exemple
x.test()

v = Exemple
color, brand = v.car('Зеленый', 'BMV')
name = v.driver('Люки')
print(v.info(name, color, brand))

