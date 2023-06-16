# Entry widget

from tkinter import *

window=Tk()
window.geometry("600x600")
#window.config()

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(int(len(entry.get())-1),END)
def submit():
    print("You entered "+ entry.get())

entry= Entry(window,fg="Black", #This is to insert the entry widget to the window
             bg="white",
             show="X",          #This shows the character when you type
             )

entry.pack()

sumbit_button=Button(window,text="submit",command=submit)
sumbit_button.pack()

delete_button=Button(window,text="delete",command=delete)
delete_button.pack()

backspace_button=Button(window,text="backspace",command=backspace)
backspace_button.pack()



window,mainloop()