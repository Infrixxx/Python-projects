#In order to create an object we need to create a class

#for small program class can be in main module
#for big program we will use a different module
#If in a different module we can import the class
#Objects have attributes and methods

class Car:

    #Attributes
    make=None
    model=None
    year=None
    color=None

    #We need a method that will create the objects, which is called the constructor
    #we use a method that uses two underscore, which is called initializer
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    #Methods
    def drive(self):
        #self refers to the object that is using this method
        #print("This car is driving")
        #Let's replace car with the name of the model that we are working with
        print("This "+self.make+" "+self.model+" is driving")
    def stop(self):
        print("This "+self.model+" is stopped")