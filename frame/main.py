# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)  #adds frame to window
frame.place(x=100,y=100)              #pack(side=BOTTOM)                             #frame is place on the bottoom of the window

Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)      #Adds Button to the top of frame
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

window.mainloop()