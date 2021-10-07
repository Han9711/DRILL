import turtle
import random


def stop():
    turtle.bye()

def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    a = (y2-y1)/(x2-x1)
    b = y1 - a * x1

    for x in range(x1, x2+1, 1):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2)

    pass


def draw_line(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    for i in range(0, 100+1, 2):
        t = i / 100
        x = (1-5)*x1 + t*x2
        y = (1-t)*y1 + t*y2
        draw_point((x, y))

    draw_point(p2)

def turtleDrawWeb(size, t, angle):
    for i in range(t):
        turtle.color(0, 1, 0)
        turtle.forward(size)
        turtle.left(angle)

prepare_turtle_canvas()

turtle.pendown()

for i in range(10):
    turtleDrawWeb(200 - 20 * i, 6, 60)

    turtle.left(60)
    turtle.forward(20)
    turtle.right(60)

for j in range(6):
    turtle.forward(250)
    turtle.backward(250)
    turtle.left(60)

turtle.penup()

turtle.done()