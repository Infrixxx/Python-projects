from tkinter import *
from tkinter.ttk import *
import time


#-----------------------------------------------------------------------------------------
#We going to add a progress bar and  a button that will fill the progress bar when clicked
#-----------------------------------------------------------------------------------------
def start():                                #function to start download
    GB = 100                                #Size of game being downloaded
    download = 0                            #Amounts of GB downloaded
    speed = 1                               #Download speed
    while(download<GB):
        time.sleep(0.05)                                        #Delay to simulate each task waiting to be completed

        bar['value']+=(speed/GB)*100                            #This is to add value to the progress bar out of the
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")            #This is to set what percent is, we
                                                                #cast to int then str so to avoid the result being cast to float
        text.set(str(download)+"/"+str(GB)+" GB completed")     #To show what task we on
        window.update_idletasks()                               #updates the window after each iteration

window = Tk()

percent = StringVar()                    #Allows us to update percent with some new text
text = StringVar()

bar = Progressbar(window,                #We add Progress bar to window
                  orient=HORIZONTAL,     #Orientation of progress bar
                  length=300)            #length of progress bar

bar.pack(pady=10)                        #adds padding to the y direction

percentLabel = Label(window,textvariable=percent).pack()     #This is top  add a percent label
                                                             #to the progress bar
taskLabel = Label(window,textvariable=text).pack()           #defines what task we currently on,
                                                             # store it to strvar

button = Button(window,text="download",command=start).pack()

window.mainloop()

