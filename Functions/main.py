# Functions= a block of code which us executed only when it is called.

#def is used to define a function followed by name and colon at the end

#def hello():
    #code under this function will belong to the function
    #print("hello"+name)
    #print("have a nice day")


#This will execute the block 3x
#hello()
#hello()
#hello()


#def hello(name):
    #print("hello "+name)
    #print("have a nice day")

#we can send the function information by putting value in the parentheses
#This are called arguments
#It needs to have the same amount/number of parameters
#hello("Tumi")

#when we call the hello function, we sending our argurment "Tumi" to the function

#we can also send variables too
#my_name='Boitumelo'

#hello(my_name)

#To send two values, we need to have two parameters to take in two arguments
#def hello(name,last_name):
    #print("hello "+name+" "+last_name)
    #print("have a nice day")

#hello('Boitumelo','Rachoshi')

#To send three values, we need to have three parameters to take in two arguments
def hello(name,last_name,age):
    print("hello "+name+" "+last_name)
    print("You are " +str(age)+" years old")
    print("have a nice day")

hello('Boitumelo','Rachoshi',21)