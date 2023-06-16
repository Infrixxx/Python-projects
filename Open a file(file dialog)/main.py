
from tkinter import *
from tkinter import filedialog

def openFile():

#***********************************************************************************************************************
    #filepath = filedialog.askopenfilename()         #filedialog.askopenfilename() opens a window which opens the
                                                    # computer to access files, this will return the file path of
                                                    #the selected path.
    #print(filepath)
#***********************************************************************************************************************
#                                           MAIN CODE FOR FUNCTION BELOW:
#***********************************************************************************************************************

    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\BC RACHOSHI\\PycharmProjects\\Open a file(file dialog)",
                                                        #initial directory, this will open the project in the main foler
                                          title="Open file okay?",            #title of the open file window
                                          filetypes= (("text files","*.txt"),   #This is type of file that can be opened
                                                                                #This will allow user to open txt only
                                          ("all files","*.*")))                 #This will look for all files
    file = open(filepath,'r')                                                   #opens the file path and r is for read
    print(file.read())                                                          #prints file and reads it
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()

