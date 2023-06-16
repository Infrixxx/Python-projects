#Variables = A container for a value, behaves as the value it contains.


#First data type we will cover is strings, strings are a series of characters.
#To create a string we can use single quotes or double quotes

name = "Boitumelo"
last_name="Rachoshi"
Middle_name="Charles"

Full_name=name+" "+Middle_name+" "+last_name
#type function is to print the data type of the variable
print(type(name)) #This will print the data type to the console window.
#You can combine variables as long as they of the same type
print("Hello"+" "+Full_name)

#different data type variable. Interger = int

age = 20
#To increase age we can do this
age=age+1 #This will print 22
#Another shortcut can be
age+=1

print(age)

#In order to print our age with a string literal we will need to convert our integer to a string
# printing this print("Your age is" + age) will not work
#printing this print("Your age is"+ str(age))  we use str to convert variable to string.
print("Your age is "+ str(age))




#float is a variable that stores numbers with decimal numbers

height=250.5
print("Your height is "+ str(height)+" cm" )


#Last data type we looking into is the boolean data type, which can only store true or false

human=False
print(human)
#Booleans are very useful when we get to if statements.
print(type(human))
human=True
print("Are you a human? "+ str(human))





#Multiple assignments= allow us to assign multiple variables using one line of code

#instead of
#cow= "black"
#age= 21

age,cow= 21,"black"

print(age)
print(cow)


#Also if variables have the same value you can do this
cake=30
bake=30
lake=30
rake=30
cake=bake=lake=rake=30
print(cake)
print(bake)
print(lake)
print(rake)
