#Class variables
#Instance
from Car import Car

#car_1=Car("chevy","Corvette",2021,"blue")
#car_2=Car("Ford", "Mustang",2022,"Red")

#car_1.wheels=2 # we modified the wheels from default,
                # this is how we access class variables


#print(car_1.wheels)
#print(car_2.wheels)

#Another way to access class variables

Car.wheels=2#This will affect it for all instances of the class

 print(Car.wheels)
