from tkinter import *

#label = an area widget that holds text and/or an image within a window

window= Tk()

photo= PhotoImage(file="nebula universe galaxy black hole.png")

# we first pass in name of window into constructer,as the master of the label

label= Label(window,text="Hello world",
                    font=("Times new roman",40,"bold"), #pass in font type,size and style
                    fg="TURQUOISE",                     #fg which is called foreground is for the color of the text
                    bg="Orange",                        #this is for the background color around the text
                    relief=RAISED,                      #This is for the border style SUNKEN,RAISED
                    bd=10,                              #Border length
                    padx=20,                            #space right and left text, between text of border
                    pady=20,                            #space above and below text, between text of border
                    image=photo,                        #This is to add photo
                    compound="center")                  #This will have our image at center of our text, can be top,
                                                        # bottom,lef or right

label.pack()                            #This will place our widget at the top center of the window
#label.place(x=0,y=0)                    #This will place our text on top left of window
                                        # the value moves it certain united to the right in x direction
                                        # and moves it down y a certain amount
window.mainloop()
