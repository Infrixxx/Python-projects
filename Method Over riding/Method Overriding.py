#Method overriding= Ability to allow a sub-class,
# to provide a specific implementation of a method that is already provided by a parent

class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
#We going to define an eat method to override the above method
    def eat(self):
        print("This rabbit is eating a carrot")
#An object will use a method that is associated with itself first before relying
#on a method inherited from a parent.

animal=Animal()
rabbit= Rabbit()

rabbit.eat()
animal.eat()