


def sey_bay():
    print("Пока\nGodbay\nAstalavista")
sey_bay()

# Плюс
def plus():
    nuns = 5
    p = nuns + 10
    print(p)
plus()

# Квадрат числа X
def square(x):
    print(f"квадрат числа {x} = {x**2}")

square(5)
square(8)

# Четное не четное
def even(x):
    if x % 2 == 0:
        print(f'{x} Четное')
    else:
        print(f'{x} Не Четное')
even(int(input()))

# Факториал
def factorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr = pr * i
    print(f'Факториал числа {i} = {pr}')
factorial(4)

# Сумма
def sum(a, b):
    print(f"{a} + {b} = {a+b}")

sum(5, 6)

# Сумма return
def sum2(a, b):
    result = a + b
    return result
g = sum2(5, 10)
print(g)

