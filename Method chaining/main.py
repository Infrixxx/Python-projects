# Method chaining:  calling multiple methods sequentially.
#                   Each call performs an action on the same object and returns self

#class Car:
    #Car has four methods
    #def turn_on(self):
        #print("You start the engine")

    #def drive(self):
        #print("You drive the car")

    #def brake(self):
        #print("You step on the brakes")

    #def turn_off(self):
        #print("You turn off the engine")

#car=Car()

#car.turn_on()
#car.drive()

#with method training
#we first need to return self under each method.
#This is in the sense that after we finish using the method
#python is going to return car

class Car:

    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car=Car()

#car.turn_on().drive()
#car.brake().turn_on()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_on()
#The backslash is a line continuation character