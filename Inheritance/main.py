# Inheritance

#Animal is the parent class
class Animal:

    alive=True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


#This is the children class
#Each class can have a unique class to it too
class Rabbit(Animal):
    def run(self):
        print("This rasbbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print('This hawk is flying')

#Now we have rabbit,fish and hawk
rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

#rabbit has function called alive,
#even though we didn't create an alive
#because we used them as children classes to the parent class of Animal
#This is due to inheritance

print(Rabbit.alive)
rabbit.run()
hawk.fly()
fish.swim()

