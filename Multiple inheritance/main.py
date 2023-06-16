# Multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):

        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Fish( Prey,Predator):
    pass

class Hawk(Predator):
    pass

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()

fish.flee()
fish.hunt()