# Prevents a user from creating an object of that class
# compels a user to override abstract methods in a child class

#Abstract class = a class which contains one or more abstract methods.
#abstract method- a method that has a declaration but does not have an implementation.

#to prevent a user from creating an object of class Vehicle
#we use from abc impport ABC, abstractmethod

from abc import ABC,abstractmethod

class Vehicle(ABC):
    #This will prevent user from creating an object of the vehicle class
    @abstractmethod #makes this class an abstract class
    def go(self):
        pass
    @abstractmethod #since this is abstract we will need to define
                    # the method again the children class
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    def stop(self):
        pass
class Motorcycle(Vehicle):
    def go(self):
        print("You drive the Motorcycle")
    def stop(self):
        pass
#vehicle=Vehicle()   #line results in error since we made the Vehicle class an abstract one
                    #with an abstarct method go
                    #Methods in an abstract class cannot be used
car=Car()
motorcycle=Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

