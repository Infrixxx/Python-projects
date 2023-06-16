#*********************************************************
class Ball:


    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        #ASSIGNING OUR ARGUMENTS
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)   #TO DRAW OUR CIRCLE, OUR DIAMETER IS
                                                                            # EQUAL IN WIDTH AND HEIGHT, SO WE PASS
                                                                            # IT TWICE

        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        # [Top left corner [W:0][H:1], Bottom right corner [W:2]*[H:3]]
        coordinates = self.canvas.coords(self.image)                #first we get cordinates
                                                                    # we have four cordinates, first two is the top
                                                                    # left corner the other two is bottom right corner

        #If statements to create boundaries


        if (coordinates[2] >= (self.canvas.winfo_width()) or coordinates[0] < 0):
                                                                                    #[2]cordinates for bottom right corner
                                                                                    #canvas.winfo_width() get width of canvas
                                                                                    #[0] is for the top left corner
            self.xVelocity = -self.xVelocity
        if (coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1] < 0):
            self.yVelocity = -self.yVelocity


        self.canvas.move(self.image,self.xVelocity,self.yVelocity)
#*********************************************************