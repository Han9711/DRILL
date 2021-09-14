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

# set screen size 
sc=turtle.Screen() 
sc.setup(500,500)

turtle.shape('turtle')
  
# call methods 
turtle.onkey(moveUp,'w') 
turtle.onkey(moveRight,'d') 
turtle.onkey(moveLeft,'a')
turtle.onkey(moveDown, 's')
turtle.onkey(restart, 'Escape')
  
# to listen by the turtle 
turtle.listen()
