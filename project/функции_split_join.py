x = input()
xl = x.split()
for i in xl:
    print(i)


y = ['gil', 'gogi', 'frank']
print('Список:', y, type(y))
# Склеиваем в строку 
y = '||'.join(y) 
print('Склейка join:', y, type(y))