a = [[1, 2, 3, 4], [10, 20, 20], [100, 200, 300]]
print(len(a))
print(a[2])
print(a[0][2])

#2-Пример
s = ["Сила", "Скорость", "Мана", "Сэксуальность"]
print(len(s))
print(s[2])
print(s[0][2], s[1][2], s[0][2])

#3-Пример
z = [[1,2,3],[4,5,6],[7,8,9]]
for i in z:
    for j in i:
        print(j, end=' ')
    print()