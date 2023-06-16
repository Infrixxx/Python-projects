#Super function()=  Function used to give access to the methods of a parent class.
#                   Returns a temporary object of a parent class when used.
#

#class Rectangle:
    #pass

#class Square(Rectangle):

#    def __init__(self,length,width):
#        self.length=length
#        self.width=width

#class Cube(Rectangle):
#   def __init__(self,length,width,height):
#
#        self.length=length
#        self.width=width
#        self.height=height



#Most lines of code were repeated in the above code,
#to make code more concise we can place the code that is similar in the parent class
#Then we will use the super() funcion to call the code
#We need to pass the arguments in the init function, being length and width

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self,length,width):
       super().__init__(length,width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height

    def Volume(self):
        return self.length*self.width*self.height

square =Square(3,3)
cube=Cube(3,3,3)

print(square.area())
print(cube.Volume())