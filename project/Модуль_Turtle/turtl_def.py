import turtle
'''
def draw_square():
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    
turtle.speed(2)

draw_square()
turtle.goto(150, 150)
draw_square()
turtle.goto(-150, -150)
draw_square()
turtle.goto(75, -75)
draw_square()
'''
turtle.speed(1)
def move(a, b):
    turtle.forward(a)
    turtle.left(b)

def draw_square(a, b):
    for i in range(4):
        move(a, b)

draw_square(20, -90)
turtle.goto(150, 150)

draw_square(100, 150) 
turtle.goto(150, 150)

draw_square(50, -30) 
turtle.goto(-150, 150)
draw_square(30, 100) 

    
