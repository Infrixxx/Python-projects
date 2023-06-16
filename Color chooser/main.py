#color chooser

from tkinter import *
from tkinter import colorchooser    #sub module so we need to import it under the main module

#******************************************************************
#CLICK FUNCTION FOR COLOR
#******************************************************************
def click():
    color = colorchooser.askcolor()   #ask color function brings up the color grid
    #print(color)                     #this will print the rgb values followed by the color code.
                                      #((R,G,B),"HEX CODE")

    #colorHex = color[1]               #Stores color Hex
    #window.config(bg=colorHex)        #The will change background color of the window
#*******************************************************************************************************
#                                        ALTERNATIVELY
#*******************************************************************************************************
    window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("420x420")
button = Button(text='click me to change color',command=click)
button.pack()
window.mainloop()