from tkinter import *
def submit():
    print(" The temperature is: "+ str(scale.get())+ " degrees celsius" )
window=Tk()

#*************************************************************
#PLACE IT BEFORE THE SCALE SO THE LABEL APPEARS ABOVETHE SCALE
#*************************************************************
hot=PhotoImage(file="hot.png")
hotLabel=Label(image=hot)
hotLabel.pack()

scale= Scale(window,from_=0,#to call a scale instance
             to=100,
             length=600,
             orient=VERTICAL, #To change orientation of scale
             font=("Times new roman",20, "italic"),
             tickinterval=10,   #inserts numeric indicators for value
             showvalue=0,       #this will hide current value
             troughcolor="Turquoise", #changes the color of the vertical column of the scale
             fg="maroon",
             bg="orange")



#scale.set(100) #This will set the initial value of the scale
#*******ALTERNATIVELY***********
scale.set(scale["from"]) #This will begin from value

scale.pack()

#*************************************************************
#PLACE IT AFTER THE SCALE SO THE LABEL APPEARS BELOW THE SCALE
#*************************************************************
cold=PhotoImage(file="cold.png")
coldLabel=Label(image=cold)
coldLabel.pack()

button = Button(window,text="submit",command=submit)
button.pack()
window.mainloop()