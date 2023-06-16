# Buttons   = You click it and it does stuff
from tkinter  import *

window=Tk()

#def click():
#    print("This button was clicked")

count=0

def click():
    global count
    count+=1        #This will add one to the count variable everytime it's clicked.
    print(count)


#****************************************************************
#button=Button(window)# This will insert a button into the window
#To add to the button constructor

photo=PhotoImage(file="Box-head-3.gif")
#below is to open button
button= Button(window,                                   #This is to define where the button will appear and specs of it
                text="Click the box",
                command=click,
                font=("Times new roman",20,"bold"),
                fg="black",
                bg="red",
                activebackground="yellow",                  #color that shows when button is clicked
                activeforeground="orange",                  #color of the text when button is clicked
                image=photo,                                #To add photo
                compound="bottom"                           #To place a photo
               )
#****************************************************************
#This is to close the button and make it appeaer in the window:
button.pack()
window.mainloop()
