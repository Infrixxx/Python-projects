#widgets = GUI elements: buttons, textboxes, labels, images
#Windows= serges as a container to hold or contain these widgets

from tkinter import *

window=Tk() #instantiate an instance of a window
#**********************************************************************************
#ALL COMMANDS NEED TO BE ADDED BEFORE THE FINAL COMMAND TO DISPLAY WINDOW ON SCREEN
#**********************************************************************************

window.geometry("700x700") #This is to change dimension of the window ("WxH")
window.title("Rachoshi terminal ")

#To use the picture in our file, we need to convert it to photoimage
icon= PhotoImage(file="Rachoshi-Holding-Logo-Base-for-mockup.gif")           #images in PGM, PPM, GIF, PNG format.

#To change color of window
window.config(background="Turquoise")    #can be a Hex value or name

#To set the picture as icon of the window, we use the following function
#we pass the photoimage of icon as an argument
window.iconphoto(True,icon)

window.mainloop()   #to display a window, we : nameofwindow.mainloop()
                    #This will place window on computer screen, listen for events



#we going to be adding widgets to the above window