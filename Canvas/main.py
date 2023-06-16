# canvas =  widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)    #since we made the width and height 500,
                                                # the top left corner is (0,0) the bottom
                                                # right corner is (500,500)

#--------------------------------------------------------------------------------------------------------
# *******************************BELOW WE CREATING TWO LINES*******************************************
# -------------------------------------------------------------------------------------------------------
#canvas.create_line(0,0,500,500,fill="blue",width=5)  #(0,0) is starting point and (500,500) ending point
                                                     #fill is to change line color and width is to change
                                                     # line thickness

#canvas.create_line(0,500,500,0,fill="red",width=5)   #This will appear on the top since it is the most
                                                     #recently created
#--------------------------------------------------------------------------------------------------------
# *******************************BELOW WE CREATING A RECTANGLE*******************************************
# -------------------------------------------------------------------------------------------------------
#canvas.create_rectangle(50,50,250,250,fill="purple")

#--------------------------------------------------------------------------------------------------------
# *******************************BELOW WE CREATING A POLYGON*******************************************
# -------------------------------------------------------------------------------------------------------
#points = [250,0,500,500,0,500]                                              #CORDINATES OF THE TRIANGLE POINTS
                                                                            #POINTS ARE IN SETS, ABOVE THERE ARE 3 SETS

#canvas.create_polygon(points,fill="yellow",outline="black",width=5)         #CREATES A TRIANGLE
#canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)             #An arc is a curve between two points,
                                                                            #used to create a circle
                                                                            #style can be CHORD,PIESLICE,ARC
                                                                            #start shifts arc around the angle
                                                                            #we can also set the extent of the arc

canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)                   #This draws an oval, first set of x and y
                                                                            #then second set of x and y
canvas.pack()

window.mainloop()
