#*********************************************************
from tkinter import *
from Ball import *          #we import everything from our ball class
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"purple")
tennis_ball = Ball(canvas,0,0,50,4,3,"Grey")
basket_ball = Ball(canvas,0,0,125,3,5,"Orange")
bowling_ball = Ball(canvas,0,0,75,2,1,"Turquoise")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()
    window.update()             #So that the window updates
    time.sleep(0.01)

window.mainloop()

