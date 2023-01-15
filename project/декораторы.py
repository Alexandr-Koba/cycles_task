

# Замыкания
def adder(x):
    def inner(n):
        return x+n
    return inner

y = adder(2)
print(y(5))
print(y(7))
print(y(10))

# Замыкания Счетчик
def count():
    c = 0
    def sum():
        nonlocal c
        c +=1
        return c

    return sum

t = count()

print(t)