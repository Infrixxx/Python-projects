#Checkbox

from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar()                    #stores the int variables from chrck button

python_photo = PhotoImage(file='Ground.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,   #returns 1 if the box is checked
                           offvalue=0,  #returns 0 if the box is not checked
                           command=display, #function
                           font=('Arial',20),
                           fg='white',
                           bg='black',
                           activeforeground='white',  #color when you click the check mark
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left') #display the picture to the left of the text
check_button.pack()


window.mainloop()