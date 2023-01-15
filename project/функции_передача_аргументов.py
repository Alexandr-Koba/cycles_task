

def f(*args):
    print(args, type(args))

f(4, 4, 4)
f('Log', [1, 2, 3, 4, 5], 1000)
f()

def s(**kwargs):
    print(kwargs)

s(a=1, b=2, c=3) 


def x(*args, **kwargs):
    print(args, kwargs)

x(1,2,3,4,5, a=9, b=8, c=7, h=6)