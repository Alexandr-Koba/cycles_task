for i in range(4):
    for j in range(4):
        print('|', end='')
        for k in range(4):
            print('_ ', end='')
    print()

#2
print('\n2 пример\n')
count = 0
for i in range(9):
    print(count +1, end='')
    count +=1
    for j in range(5):
        print('|', end='')
        for j in range(4):
            print('_', end='')
    print('|')

#3
print("3 Пример")
count = 0
for w in range(3):
    print(count +1, end='')
    count +=1
    for p in range(2):
        print(':', end='')
        for s in range(5):
            print('_', end='')
    print()