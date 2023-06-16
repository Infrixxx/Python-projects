#Concept where the class of an object is less important than the methods\attributes
#           Class types are not checked if minimum methods are met.
#           "if it walks like a duck, and it quacks like a duck, then it must be a duck


class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck=Duck()
chicken=Chicken()
person=Person()

person.catch(chicken)

