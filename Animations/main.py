from tkinter import *
import time

#---------------------------------------------------------------------
#************************CONSTANTS************************************
#---------------------------------------------------------------------
WIDTH = 500
HEIGHT = 500
xVelocity = 1                       #how fast image is moving on x axis
yVelocity = 1                         #how fast image is moving on y axis
window = Tk()

#-------------------------------------------------------------------------
#                   CREATING THE CANVAS
#-------------------------------------------------------------------------
canvas = Canvas(window,width=WIDTH,height=HEIGHT)       #DIMENSIONS OF THE CANVAS
canvas.pack()

#-------------------------------------------------------------------------
#               IMPORTING THE IMAGES
#-------------------------------------------------------------------------

background_photo = PhotoImage(file='space.png')z
background = canvas.create_image(0,0,image=background_photo,anchor=NW)              #image on top left corner

photo_image = PhotoImage(file='UFO.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()                                       # .width  retireves width of the image
image_height = photo_image.height()                                     # .height retireves height of the image

while True:
    coordinates = canvas.coords(my_image)                               #retrieves cordinates of image
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):        #[0] is for  x-cordinates,we also need to factor
                                                                        #in the width of the image
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity


    canvas.move(my_image,xVelocity,yVelocity)                           #takes what we moving,how far we want to
                                                                        #move image on each axis

    window.update()
    time.sleep(0.01)                                                    #we make it sleep for certain amount of seconds

window.mainloop()