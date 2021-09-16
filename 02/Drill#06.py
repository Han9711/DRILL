import os
os.chdir('d:/DRILL/Rendering')
os.getcwd()

from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

def moveSquare():
    x=0
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    y=90
    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(790, y)
        y = y + 2
        delay(0.01)

    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 590)
        x = x - 2
        delay(0.01)

    while (y >90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(5, y)
        y = y - 2
        delay(0.01)

def moveCircle():
    x=400
    y=300
    t=0
    
    while (t<180):
        rx = x+210*(math.sin(t/360*2*math.pi))
        ry = y-210*(math.cos(t/360*2*math.pi))
        t=t+1

        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(rx, ry)
        
        delay(0.01)

    while (t>0):
        rx = x-210*(math.sin((180-t)/360*2*math.pi))
        ry = y+210*(math.cos((180-t)/360*2*math.pi))
        t=t-1

        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(rx, ry)
        
        delay(0.01)

while(True): 
    moveSquare()
    moveCircle()

close_canvas()
