from tkinter import *

def drag_start(event):                              #takes our event
    widget = event.widget                           #Gets widget of event we are dealing with
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
#---------------------------------------------------------------------------------------------------
#***************************   CREATE NEW X AND Y CORDINATES   *************************************
#---------------------------------------------------------------------------------------------------
    x = widget.winfo_x() - widget.startX + event.x   # .winfo_x() will get top x left cordinate relative
                                                     #to the window we are in
                                                     #startX place where we click within the label itself
                                                     #event.X where we dragging it to

    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()

label = Label(window,bg="red",width=10,height=5)    #we created a label of height 5 and width 10
label.place(x=0,y=0)                                #situated at the top left corner of our screen

label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_start)                 #event tied to the left button click, so click with
                                                    #left button will call our drag_start function
label.bind("<B1-Motion>",drag_motion)               #When we hold down left mouse button and drag

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)
window.geometry("600x600")
window.mainloop()
