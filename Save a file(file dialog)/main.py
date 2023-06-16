from tkinter import *
from tkinter import filedialog

#****Function to save file****
def saveFile():

    file = filedialog.asksaveasfile(initialdir="C:\\Users\\BC RACHOSHI\\PycharmProjects\\Save a file(file dialog)",
                                    defaultextension='.txt',                            #initial extension
                                    filetypes=[                                         #types of files hat can be saved
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:            #This is if we decide not to save and exit, we wont get an error
        return
    filetext = str(text.get(1.0,END))   #retrieves text from text box and converts to string
    #filetext = input("Enter some text I guess: ") #//use this if you want to use console window
    file.write(filetext)                #writes text into file
    file.close()                        #closes file

window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
