# Multi-level inheritance is when a derived class(child) inherits another derived class(child)

#Lets create a family tree of organisms

class Organisms:

    alive=True

class Animal(Organisms):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This animal is barking")

dog=Dog()
print(dog.alive)
dog.eat()
dog.bark()