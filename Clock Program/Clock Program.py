# Clock Program

from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")           #strftime retrieves current time tuple  and allows us to
                                                    # format it as we want, to a string as specified by the
                                                    # format argument
    time_label.config(text=time_string)             #adds the text to the label : time_label

    day_string = strftime("%A")

    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    #we going to perform a recursive function in which we call a function within itself, we calling update within update
    window.after(1000, update)                    #window.after causes a 1000 millisecond delay before calling
                                                  #the function update, after the delay, this is after a second

window=Tk()

time_label=Label(window,font=("Calibri",50,"bold"),fg="white",bg="Brown")
time_label.pack()

day_label = Label(window,font=("Goth",25,"bold"),fg="brown")
day_label.pack()

date_label = Label(window,font=("Ink Free",30),bg="brown",fg="white")
date_label.pack()

update()
window.mainloop()
