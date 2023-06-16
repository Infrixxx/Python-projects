#Object orientated programming
#Object= Instance of a class

from Car import Car

#We pass in four arguments despite the function requiring us to
#pass in 5 arguments as self is automatically passed in for us.

car_1=Car("For Car 1:\n\nchevy","Corvette",2021,"blue")


print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
print('\n \nFor Car 2:\n')

#we do not need to pass in self, since it is done automatically
#So when we call the drive() function, the argument is passed


# We can use the class to create more car objects
car_2=Car("Ford", "Mustang",2022,"Red")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.stop()