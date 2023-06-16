#A menu bar is a graphical control element which contains drop-down menus


from tkinter import *

def openFile():
    print("File has been opened!")
def saveFile():
    print("File has been saved!")
def cut():
    print("You cut some text!")
def copy():
    print("You copied some text!")
def paste():
    print("You pasted some text!")

window = Tk()

openImage = PhotoImage(file="file.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")

menubar = Menu(window)          #This adds menubar to the window
window.config(menu=menubar)     #This is to set the menu of the window to be equal to that of the menubar

#***********************************************************************************
#----------------------------TO ADD MENUS TO THE MENU BAR---------------------------
#***********************************************************************************

fileMenu = Menu(menubar,                #This is to add the file menu to our menubar
                tearoff=0,              #removes the tearoff
                font=("MV Boli",15))


#----------------------- ADD DROP DOWN EFFECT TO MENU BAR---------------------------


menubar.add_cascade(label="File",                 #menubar.add_cascade() has a Drop down menu effect
                    menu=fileMenu)                #menu of this file will be equal to the file menu we created

#-----------------------Adding commands to the fileMenu--------------------------------------

fileMenu.add_command(label="Open",      #Name of the command
                     command=openFile,
                     image=openImage,
                     compound='left')

fileMenu.add_command(label="Save",
                     command=saveFile,
                     image=saveImage,
                     compound='left')

fileMenu.add_separator()                    #Adds a line to seperate the menu below this line

fileMenu.add_command(label="Exit",
                     command=quit,          #The quit command closes the window.
                     image=exitImage,
                     compound='left')


#--------------------THIS IS FOR ADDING EDIT MENU TO MENUBAR-------------------------------------

editMenu = Menu(menubar,                #adds edit menu to menubar
                tearoff=0,              #0= false, this removes the tearoff line from the menubar
                font=("MV Boli",15))

menubar.add_cascade(label="Edit",
                    menu=editMenu)


#-----------------------Adding commands to the editMenu-----------------------------------------

editMenu.add_command(label="Cut",
                     command=cut)

editMenu.add_command(label="Copy"
                     ,command=copy)

editMenu.add_command(label="Paste",
                     command=paste)

#---------------------------Adding view menu---------------------------------------------
viewMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="View",menu=viewMenu)

viewMenu.add_command(label="Tool")
viewMenu.add_command(label="Appearace")

window.mainloop()
