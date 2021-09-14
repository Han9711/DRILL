import turtle

def moveUp():
    turtle.setheading(90)
    turtle.forward(50) 
      
def moveRight(): 
    turtle.setheading(0)
    turtle.forward(50)
  
def moveLeft(): 
    turtle.setheading(180)
    turtle.forward(50)

def moveDown(): 
    turtle.setheading(270)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape('turtle')
  

turtle.onkey(moveUp,'w') 
turtle.onkey(moveRight,'d') 
turtle.onkey(moveLeft,'a')
turtle.onkey(moveDown, 's')
turtle.onkey(restart, 'Escape')
  

turtle.listen()

