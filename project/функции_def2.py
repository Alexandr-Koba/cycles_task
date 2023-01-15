
# Возвращает квадрат числа Х (10 раз)
def square(x):
    return x**2

for _ in range(11):    
    a = square(int(input()))
    print(a)
