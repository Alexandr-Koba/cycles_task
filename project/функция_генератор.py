
# Обычная функция
def f():
    return[42, 33, 11]

print(f())


# Функция генератор
def genf():
    for i in [42, 33, 11]:
        yield i

s = genf()

print(s)

print('NEXT')
print(next(s)) 
print(next(s)) # Последовательно выводит значения с каждым вызовом
print(next(s))


