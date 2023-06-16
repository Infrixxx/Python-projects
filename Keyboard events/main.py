from tkinter import *

def doSomething(event):
    #print("You pressed: " + event.keysym)       #To display button pressed we use event.keysm
    label.config(text=event.keysym)            #editing label to display key we press

window = Tk()

window.bind("<Key>",doSomething)                 #Two arguments taken by the window function,
                                                 #To have functions respond to all keys we type <Key>
                                                 # window.bind(event,function)
#window.bind("<Return>", doSomething)            # Return works when we press enter
window.geometry("600x600")
label = Label(window,font=("Helvetica",100))     #label to display whatever key we press
label.pack()

window.mainloop()



