# Таблица умножения с помощью вложенных циклов и функции range()

for j in range(1, 10):
    for i in range(1, 11):
        print(i, '*', j, '=', i*j, end='  ')
        print()
    print() 