import turtle
turtle.reset()
turtle.penup()
turtle.goto(-100, 300)
turtle.pendown()
count = 6
while (count > 0):
	turtle.forward(500)
	turtle.back(500)
	turtle.penup()
	turtle.right(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.pendown()
	count -= 1

turtle.penup()
turtle.goto(-100, 300)
turtle.right(90)
turtle.pendown()
count = 6
while (count > 0):
	turtle.forward(500)
	turtle.back(500)
	turtle.penup()
	turtle.left(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.pendown()
	count -= 1

turtle.exitonclick()

